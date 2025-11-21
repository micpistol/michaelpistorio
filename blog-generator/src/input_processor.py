"""
Input Processor for Blog Post Generator
Handles: URLs, PDFs, images, plain text, transcripts, academic papers
"""

import os
import re
from pathlib import Path
from typing import Dict, Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import PyPDF2
import pdfplumber
from PIL import Image
import pytesseract


class InputProcessor:
    """Process various input types and extract text content"""

    def __init__(self, config: Dict):
        self.config = config
        self.timeout = config.get('processing', {}).get('fetch_timeout', 30)
        self.max_image_size = config.get('processing', {}).get('max_image_size', 5242880)

    def process(self, input_path: str) -> Dict[str, any]:
        """
        Main entry point - detects input type and processes accordingly

        Returns:
            {
                'content': str,  # Extracted text content
                'source_type': str,  # Type of input
                'metadata': dict,  # Any extracted metadata
                'title': Optional[str],  # Auto-detected title
            }
        """
        # Detect input type
        if self._is_url(input_path):
            return self._process_url(input_path)

        path = Path(input_path)
        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        suffix = path.suffix.lower()

        if suffix == '.pdf':
            return self._process_pdf(path)
        elif suffix in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:
            return self._process_image(path)
        elif suffix in ['.txt', '.md', '.markdown']:
            return self._process_text_file(path)
        else:
            # Try to process as text
            return self._process_text_file(path)

    def _is_url(self, text: str) -> bool:
        """Check if input is a URL"""
        try:
            result = urlparse(text)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def _process_url(self, url: str) -> Dict:
        """Process web URL - fetch and extract content"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove script and style elements
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()

            # Try to extract title
            title = None
            if soup.title:
                title = soup.title.string
            elif soup.find('h1'):
                title = soup.find('h1').get_text()

            # Extract main content
            # Try common article containers
            article = soup.find('article') or soup.find('main') or soup.find('body')

            if article:
                text = article.get_text(separator='\n', strip=True)
            else:
                text = soup.get_text(separator='\n', strip=True)

            # Clean up text
            text = self._clean_text(text)

            return {
                'content': text,
                'source_type': 'url',
                'metadata': {
                    'url': url,
                    'domain': urlparse(url).netloc
                },
                'title': title
            }

        except Exception as e:
            raise Exception(f"Error processing URL: {str(e)}")

    def _process_pdf(self, path: Path) -> Dict:
        """Process PDF file - extract text and metadata"""
        content_parts = []
        metadata = {}
        title = None

        try:
            # Try pdfplumber first (better for complex PDFs)
            with pdfplumber.open(path) as pdf:
                # Extract metadata
                if pdf.metadata:
                    metadata = {
                        'title': pdf.metadata.get('Title'),
                        'author': pdf.metadata.get('Author'),
                        'subject': pdf.metadata.get('Subject'),
                        'pages': len(pdf.pages)
                    }
                    title = metadata.get('title')

                # Extract text from all pages
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        content_parts.append(text)

            content = '\n\n'.join(content_parts)

            # If pdfplumber fails, fall back to PyPDF2
            if not content.strip():
                with open(path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)

                    if not metadata:
                        pdf_metadata = reader.metadata
                        if pdf_metadata:
                            metadata = {
                                'title': pdf_metadata.get('/Title'),
                                'author': pdf_metadata.get('/Author'),
                                'subject': pdf_metadata.get('/Subject'),
                                'pages': len(reader.pages)
                            }
                            title = metadata.get('title')

                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            content_parts.append(text)

                content = '\n\n'.join(content_parts)

            content = self._clean_text(content)

            # Try to extract title from first lines if not in metadata
            if not title and content:
                lines = content.split('\n')
                for line in lines[:10]:
                    if len(line.strip()) > 10 and len(line.strip()) < 200:
                        title = line.strip()
                        break

            return {
                'content': content,
                'source_type': 'pdf',
                'metadata': metadata,
                'title': title
            }

        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")

    def _process_image(self, path: Path) -> Dict:
        """Process image file - OCR to extract text"""
        try:
            # Check file size
            if path.stat().st_size > self.max_image_size:
                raise ValueError(f"Image too large (max {self.max_image_size / 1024 / 1024}MB)")

            # Open and process image
            image = Image.open(path)

            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Extract text using OCR
            ocr_lang = self.config.get('processing', {}).get('ocr_language', 'eng')
            text = pytesseract.image_to_string(image, lang=ocr_lang)

            text = self._clean_text(text)

            # Try to detect if it's a Reddit screenshot
            is_reddit = 'reddit' in text.lower() or 'r/' in text.lower()

            return {
                'content': text,
                'source_type': 'image_ocr',
                'metadata': {
                    'image_size': image.size,
                    'format': image.format,
                    'is_reddit_screenshot': is_reddit
                },
                'title': None
            }

        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")

    def _process_text_file(self, path: Path) -> Dict:
        """Process plain text or markdown file"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Detect if it's a transcript (common patterns)
            is_transcript = any([
                '[' in content and ']' in content,  # Timestamps
                'Speaker' in content,
                content.count(':') > 20,  # Multiple speaker markers
            ])

            # Try to extract title from first line
            title = None
            lines = content.split('\n')
            first_line = lines[0].strip() if lines else ''
            if first_line and not first_line.startswith('#'):
                title = first_line
            elif first_line.startswith('# '):
                title = first_line[2:].strip()

            return {
                'content': content,
                'source_type': 'transcript' if is_transcript else 'text',
                'metadata': {
                    'filename': path.name,
                    'is_transcript': is_transcript
                },
                'title': title
            }

        except Exception as e:
            raise Exception(f"Error processing text file: {str(e)}")

    def _clean_text(self, text: str) -> str:
        """Clean and normalize extracted text"""
        # Remove excessive whitespace
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        text = re.sub(r' +', ' ', text)

        # Remove common artifacts
        text = text.replace('\x00', '')
        text = text.replace('\uf0b7', '•')  # Fix bullet points

        return text.strip()

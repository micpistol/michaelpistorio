# Blog Post Generator

A powerful, AI-driven tool that transforms any content into polished blog posts for your website. Feed it PDFs, web links, images, transcripts, or plain text, and get publication-ready HTML in minutes.

## ✨ Features

- **Universal Input Support**: URLs, PDFs, images (with OCR), transcripts, academic papers, plain text
- **AI-Powered Generation**: Uses Claude AI to write engaging, well-structured blog posts
- **Your Site's Style**: Automatically formats posts to match your existing design
- **Interactive Editing**: Refine the generated content with AI assistance
- **One Command**: From input to HTML in a single command
- **Markdown + HTML**: Outputs both formats for flexibility

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd blog-generator
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Get your API key from: https://console.anthropic.com/

### 3. Check Setup

```bash
python generate.py check
```

### 4. Generate Your First Post

```bash
# From a PDF
python generate.py generate paper.pdf

# From a URL
python generate.py generate https://example.com/article

# From a screenshot
python generate.py generate screenshot.png

# From plain text
python generate.py generate notes.txt
```

## 📖 Usage Guide

### Basic Command

```bash
python generate.py generate <input>
```

### With Options

```bash
# Add custom instructions
python generate.py generate paper.pdf --prompt "Focus on practical applications"

# Override the title
python generate.py generate article.pdf --title "My Custom Title"

# Set category
python generate.py generate notes.txt --category "Tutorial"

# Skip interactive editing
python generate.py generate transcript.txt --no-edit

# Custom output path
python generate.py generate input.pdf --output my-post.html
```

### Interactive Editing

After generation, you'll enter an interactive mode where you can:

- **continue**: Proceed to save the post
- **edit-title**: Change the title
- **edit-category**: Change the category
- **refine**: Ask AI to refine the content based on your feedback
- **preview**: View the full content
- **quit**: Cancel and exit

Example refine workflow:

```
What would you like to do? refine
What would you like to change? Make the introduction more engaging and add more examples
[AI refines the content...]
✓ Content refined

What would you like to do? preview
[Shows full content...]

What would you like to do? continue
✓ Blog post generated successfully!
```

### Convert Existing Markdown

If you already have markdown files with frontmatter:

```bash
python generate.py convert my-post.md
```

## 📁 Input Types

### 1. Web URLs

Automatically extracts article content, cleans up navigation/ads:

```bash
python generate.py generate https://arxiv.org/abs/2301.12597
```

### 2. PDFs

Extracts text and metadata from research papers, reports, etc.:

```bash
python generate.py generate research-paper.pdf
```

### 3. Images (Screenshots)

Uses OCR to extract text from images (great for Reddit comments, tweets):

```bash
python generate.py generate reddit-comment.png
```

**Note**: Requires `tesseract` OCR engine:
- macOS: `brew install tesseract`
- Ubuntu: `sudo apt-get install tesseract-ocr`
- Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki

### 4. Plain Text / Transcripts

Processes text files, interview transcripts, meeting notes:

```bash
python generate.py generate interview-transcript.txt
```

### 5. Markdown

Processes existing markdown files:

```bash
python generate.py generate draft-post.md
```

## 📝 Output

Each generation creates two files:

1. **HTML**: `essay-title-slug.html` - Ready to publish on your site
2. **Markdown**: `essay-title-slug.md` - With frontmatter for future edits

Example output structure:

```markdown
---
title: The Future of Neural Rendering
category: Research
excerpt: A comprehensive look at how neural rendering is transforming VFX
tags: neural-rendering, ai, vfx
date: 2025-01-15
---

[Your generated blog post content in markdown...]
```

## 🎨 Customization

### Configure Settings

Edit `config.yaml` to customize:

```yaml
# Site settings
site:
  author: "Your Name"
  base_url: "https://yoursite.com"

# Default metadata
defaults:
  category: "Research"
  reading_speed: 200  # words per minute

# Generation settings
generation:
  model: "claude-sonnet-4"
  temperature: 0.7
  max_tokens: 4000
```

### Modify HTML Template

Edit `src/html_generator.py` to change:
- CSS styles
- Layout structure
- Meta tags
- Navigation

### Adjust AI Behavior

Edit the system prompt in `src/ai_generator.py` to change:
- Writing style
- Content structure
- Tone and voice

## 🔧 Workflow Examples

### Example 1: Academic Paper to Blog Post

```bash
# Download a paper
curl -o paper.pdf https://arxiv.org/pdf/2301.12597.pdf

# Generate blog post with focus on practical implications
python generate.py generate paper.pdf \
  --prompt "Explain this for practitioners, focus on practical applications" \
  --category "Research"

# Review and refine interactively
# Choose "refine" to adjust tone or add examples
# Choose "continue" when satisfied

# Output: essay-neural-rendering-breakthrough.html
```

### Example 2: Reddit Thread to Commentary

```bash
# Take screenshot of interesting Reddit thread
# Save as reddit-discussion.png

# Generate post analyzing the discussion
python generate.py generate reddit-discussion.png \
  --prompt "Analyze this discussion and provide expert commentary" \
  --category "Analysis"
```

### Example 3: Interview Transcript to Article

```bash
# You have: interview-transcript.txt

python generate.py generate interview-transcript.txt \
  --prompt "Turn this into a narrative article with key quotes highlighted" \
  --title "Conversation with [Expert Name]" \
  --category "Interview"
```

### Example 4: Quick Text Notes to Post

```bash
# You have some notes: ideas.txt

python generate.py generate ideas.txt \
  --prompt "Expand these notes into a thoughtful essay with examples"
```

## 📚 Advanced Usage

### Batch Processing

Generate posts from multiple inputs:

```bash
# Create a script
for file in papers/*.pdf; do
  python generate.py generate "$file" --no-edit
done
```

### Custom Prompts for Different Content Types

```bash
# For technical deep-dives
--prompt "Provide detailed technical analysis with code examples"

# For beginner-friendly content
--prompt "Explain concepts simply for newcomers, use analogies"

# For opinion pieces
--prompt "Write this as a thoughtful opinion piece with personal insights"

# For news/updates
--prompt "Present this as a news update with key takeaways"
```

### Integration with Workflow

```bash
# Add to your publishing workflow
python generate.py generate input.pdf --no-edit --output ../essay-new.html
cp essay-new.html /path/to/website/
git add essay-new.html
git commit -m "Add new blog post"
git push
```

## 🐛 Troubleshooting

### API Key Issues

```
Error: ANTHROPIC_API_KEY not found
```

**Solution**: Create `.env` file with your API key (see Quick Start)

### PDF Processing Fails

```
Error processing PDF: ...
```

**Solution**: Try installing pdfplumber dependencies:
```bash
pip install --upgrade pdfplumber pypdf2
```

### Image OCR Not Working

```
Error: Tesseract not found
```

**Solution**: Install Tesseract OCR engine (see Input Types section)

### "Could not extract content"

**Solution**: The input might be empty or unsupported format. Try:
- For URLs: Check if the page requires JavaScript (not supported)
- For PDFs: Ensure it's not a scanned image (try OCR on images instead)
- For images: Ensure text is clear and readable

### Dependencies Issues

```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt

# Check what's missing
python generate.py check
```

## 🎯 Best Practices

### 1. Write Good Prompts

Instead of:
```bash
--prompt "make it better"
```

Try:
```bash
--prompt "Add more concrete examples, simplify the introduction, and include a practical tutorial section"
```

### 2. Use Categories Consistently

Stick to these categories for consistency:
- **Introduction**: Overview and introductory posts
- **Research**: Deep technical analysis
- **Tutorial**: Step-by-step guides
- **Analysis**: Commentary and critique
- **Vision**: Future-looking thought pieces

### 3. Review Before Publishing

Always review generated content:
1. Check technical accuracy
2. Verify links and references
3. Test HTML in browser
4. Proofread for typos
5. Ensure images are referenced correctly

### 4. Iterate with Refine

Use the interactive refine feature:
```
What would you like to change?
> Add a section about real-world applications in VFX studios

[AI adds the section...]

What would you like to change?
> Make the conclusion more forward-looking
```

### 5. Save Your Markdown

The generated `.md` files are great for:
- Future edits
- Version control
- Sharing drafts
- Converting to other formats

## 📦 Project Structure

```
blog-generator/
├── generate.py           # Main CLI tool
├── requirements.txt      # Python dependencies
├── config.yaml          # Configuration
├── .env                 # API keys (create this)
├── src/
│   ├── input_processor.py   # Handles all input types
│   ├── ai_generator.py      # Claude AI integration
│   └── html_generator.py    # HTML output
├── examples/            # Example inputs
└── README.md           # This file
```

## 🚢 Publishing Workflow

1. **Generate**: `python generate.py generate input.pdf`
2. **Review**: Open generated HTML in browser
3. **Refine**: Use interactive editing if needed
4. **Copy**: Move HTML to your site directory
5. **Update Index**: Add to your `writing.html` page
6. **Deploy**: Commit and push to GitHub

## 💡 Tips

- **Start with good source material**: Better input = better output
- **Be specific in prompts**: Tell Claude exactly what you want
- **Use refine iteratively**: Don't try to fix everything at once
- **Save intermediate versions**: Keep the markdown files
- **Experiment with different inputs**: Try various content types

## 🔮 Future Enhancements

Potential additions:
- Automatic index page updates
- RSS feed generation
- Social media card generation
- Multi-post generation from long documents
- Web interface for non-technical users
- Template variations
- SEO optimization
- Analytics integration

## 📄 License

This tool is for personal use on Michael Pistorio's website.

## 🙏 Credits

Built with:
- [Anthropic Claude](https://www.anthropic.com/) - AI generation
- [Rich](https://github.com/Textualize/rich) - Beautiful CLI
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Web scraping
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF processing

---

**Need help?** Check the troubleshooting section or review the examples above.

**Ready to generate?** Run `python generate.py generate <your-input>`

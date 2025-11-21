"""
HTML Generator for Blog Posts
Converts markdown to HTML with site styling
"""

import re
from datetime import datetime
from typing import Dict, Optional
import markdown
from markdown.extensions import tables, fenced_code, codehilite


class HTMLGenerator:
    """Generate HTML files from blog post content"""

    def __init__(self, config: Dict):
        self.config = config
        self.author = config.get('site', {}).get('author', 'Michael Pistorio')
        self.reading_speed = config.get('defaults', {}).get('reading_speed', 200)

        # Configure markdown processor
        self.md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'nl2br',
            'sane_lists'
        ])

    def generate_html(
        self,
        title: str,
        content: str,
        excerpt: str,
        category: str,
        date: Optional[str] = None,
        slug: Optional[str] = None,
        prev_link: Optional[str] = None,
        next_link: Optional[str] = None
    ) -> str:
        """
        Generate complete HTML file from blog post data

        Args:
            title: Blog post title
            content: Markdown content
            excerpt: Short description
            category: Post category
            date: Publication date (YYYY-MM-DD) or None for today
            slug: URL slug or None to auto-generate
            prev_link: Previous post link (optional)
            next_link: Next post link (optional)

        Returns:
            Complete HTML string ready to save
        """

        # Process date
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %Y')

        # Generate slug if not provided
        if not slug:
            slug = self._slugify(title)

        # Convert markdown to HTML
        html_content = self._process_markdown(content)

        # Calculate reading time
        word_count = len(content.split())
        reading_time = max(1, round(word_count / self.reading_speed))

        # Build navigation
        nav_html = self._build_navigation(prev_link, next_link)

        # Build complete HTML
        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | {self.author}</title>
  <meta name="description" content="{excerpt}">
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{excerpt}" />
  <meta property="og:type" content="article" />
  <style>
    :root {{
      --bg:#ffffff;
      --card:#fafafa;
      --text:#1f2937;
      --muted:#6b7280;
      --accent:#1e3a8a;
      --cyan:#06b6d4;
      --border:#e5e7eb;
    }}
    html,body{{margin:0;padding:0;background:var(--bg);color:var(--text);font:17px/1.8 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}}
    .article-wrap{{max-width:740px;margin:0 auto;padding:60px 20px}}
    .article-header{{border-bottom:1px solid var(--border);padding-bottom:32px;margin-bottom:40px}}
    .article-meta{{display:flex;gap:16px;align-items:center;margin-bottom:20px;font-size:14px;color:var(--muted)}}
    .article-tag{{background:rgba(76,201,240,0.15);color:var(--accent);padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px}}
    h1{{margin:0 0 20px;font-size:clamp(32px,5vw,44px);line-height:1.2;letter-spacing:-0.5px}}
    .article-lede{{font-size:20px;color:var(--muted);line-height:1.6;margin:0}}
    .article-content h2{{font-size:28px;margin:48px 0 20px;color:var(--text);letter-spacing:-0.3px}}
    .article-content h3{{font-size:22px;margin:36px 0 16px;color:var(--accent)}}
    .article-content p{{margin:20px 0;color:var(--muted)}}
    .article-content strong{{color:var(--text);font-weight:600}}
    .article-content a{{color:var(--cyan);text-decoration:none;border-bottom:1px solid rgba(6,182,212,0.3)}}
    .article-content a:hover{{border-bottom-color:var(--cyan)}}
    .article-content ul,.article-content ol{{margin:20px 0;padding-left:24px;color:var(--muted)}}
    .article-content li{{margin:8px 0}}
    .article-content code{{background:var(--card);padding:2px 6px;border-radius:3px;font-size:0.9em;font-family:Monaco,Consolas,monospace;color:var(--accent)}}
    .article-content pre{{background:var(--card);padding:20px;border-radius:8px;overflow-x:auto;margin:24px 0}}
    .article-content pre code{{background:none;padding:0}}
    .callout{{background:var(--card);border-left:4px solid var(--accent);border-radius:8px;padding:24px 28px;margin:32px 0}}
    .callout h4{{margin:0 0 12px;color:var(--accent);font-size:14px;text-transform:uppercase;letter-spacing:0.5px}}
    .callout p{{margin:0;color:var(--muted)}}
    .pull-quote{{font-size:24px;line-height:1.5;color:var(--accent);font-style:italic;margin:40px 0;padding:24px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);text-align:center}}
    .trajectory{{background:linear-gradient(135deg, #1a1d2a 0%, #0f1115 100%);border:1px solid var(--border);border-radius:16px;padding:32px;margin:48px 0}}
    .trajectory h3{{margin:0 0 16px;color:var(--cyan);font-size:22px}}
    .trajectory p,.trajectory ul,.trajectory li{{color:#d1d5db}}
    .article-footer{{margin-top:60px;padding-top:32px;border-top:1px solid var(--border)}}
    .footer-nav{{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}
    .footer-nav a{{color:var(--accent);text-decoration:none;font-size:15px}}
    .footer-nav a:hover{{text-decoration:underline}}
    nav{{margin:20px auto;padding:16px 0;border-bottom:1px solid var(--border);max-width:740px}}
    nav a{{margin-right:24px;color:var(--muted);font-size:14px;text-transform:uppercase;letter-spacing:0.5px;text-decoration:none}}
    nav a:hover{{color:var(--accent)}}
  </style>
</head>
<body>
  <nav style="padding-left:20px;padding-right:20px">
    <a href="index.html">← Back to Work</a> |
    <a href="writing.html">All Writing</a>
  </nav>

  <article class="article-wrap">
    <header class="article-header">
      <div class="article-meta">
        <span class="article-tag">{category}</span>
        <span>{reading_time} min read</span>
        <span>{formatted_date}</span>
      </div>
      <h1>{title}</h1>
      <p class="article-lede">{excerpt}</p>
    </header>

    <div class="article-content">
{html_content}
    </div>

    <div class="article-footer">
{nav_html}
    </div>
  </article>
</body>
</html>"""

        return html

    def _process_markdown(self, content: str) -> str:
        """Convert markdown to HTML with special handling for callouts and quotes"""

        # First, handle special blockquote syntax
        content = self._process_callouts(content)
        content = self._process_pull_quotes(content)
        content = self._process_trajectory(content)

        # Convert markdown to HTML
        html = self.md.convert(content)

        # Add proper indentation
        lines = html.split('\n')
        indented = ['      ' + line if line.strip() else '' for line in lines]
        return '\n'.join(indented)

    def _process_callouts(self, content: str) -> str:
        """Process callout boxes (blockquotes with bold headers)"""

        # Pattern: > **Header**\n> Content
        pattern = r'> \*\*(.+?)\*\*\n((?:> .+\n?)+)'

        def replace_callout(match):
            header = match.group(1)
            body_lines = match.group(2).split('\n')
            body = ' '.join(line.replace('> ', '') for line in body_lines if line.strip())

            return f'<div class="callout"><h4>{header}</h4><p>{body}</p></div>'

        return re.sub(pattern, replace_callout, content)

    def _process_pull_quotes(self, content: str) -> str:
        """Process pull quotes (blockquotes with italic text)"""

        # Pattern: > *"Quote text"*
        pattern = r'> \*"(.+?)"\*'

        def replace_quote(match):
            quote = match.group(1)
            return f'<p class="pull-quote">"{quote}"</p>'

        return re.sub(pattern, replace_quote, content)

    def _process_trajectory(self, content: str) -> str:
        """Process trajectory sections (special dark sections)"""

        # Pattern: ## Trajectory (heading followed by content)
        pattern = r'## Trajectory\n\n(.+?)(?=\n##|\Z)'

        def replace_trajectory(match):
            body = match.group(1)
            # Convert the body markdown to HTML
            body_html = self.md.convert(body)
            return f'<div class="trajectory"><h3>Trajectory</h3>{body_html}</div>'

        return re.sub(pattern, replace_trajectory, content, flags=re.DOTALL)

    def _build_navigation(
        self,
        prev_link: Optional[str],
        next_link: Optional[str]
    ) -> str:
        """Build footer navigation HTML"""

        if not prev_link and not next_link:
            return ''

        nav_items = []

        if prev_link:
            nav_items.append(f'        <a href="{prev_link}">← Previous</a>')
        else:
            nav_items.append('        <span></span>')

        if next_link:
            nav_items.append(f'        <a href="{next_link}">Next →</a>')
        else:
            nav_items.append('        <span></span>')

        return f"""      <div class="footer-nav">
{chr(10).join(nav_items)}
      </div>"""

    def _slugify(self, text: str) -> str:
        """Convert title to URL-friendly slug"""
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')

    def save_html(self, html: str, output_path: str):
        """Save HTML to file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

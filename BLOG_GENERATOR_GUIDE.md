# Blog Post Generator - Implementation Guide

This document outlines what a blog post generator should do, with code examples for the current HTML structure.

---

## WHAT THE GENERATOR SHOULD PRODUCE

A blog post generator for this site should:

1. **Input:** Markdown file with YAML frontmatter
2. **Process:** Parse metadata, calculate read time, convert to HTML
3. **Output:** Standalone HTML file matching the current design pattern

---

## EXAMPLE INPUT: Markdown Source File

**File:** `content/essays/essay-sample.md`

```markdown
---
title: "How Neural Rendering Redefines Look Development"
slug: "neural-rendering-look-development"
date: "2025-01-15"
category: "Neural Rendering"
excerpt: "From NeRFs to neural BRDFs—exploring production-ready applications of neural rendering in VFX workflows."
readingTime: 12
tags: ["neural-rendering", "vfx", "production", "ai"]
series: "Intelligent VFX Futures"
seriesPart: 3
featured: true
image: "/images/neural-rendering-hero.jpg"
---

## Introduction

This is the introduction section. Markdown content here.

### Subsection

More markdown content with **bold** and *italic*.

## Key Concept

> This is a key concept that should be highlighted in a callout box.

## Conclusion

Final thoughts and forward-looking trajectory.
```

---

## EXAMPLE OUTPUT: Generated HTML File

**File:** `neural-rendering-look-development.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>How Neural Rendering Redefines Look Development | Michael Pistorio</title>
  <meta name="description" content="From NeRFs to neural BRDFs—exploring production-ready applications of neural rendering in VFX workflows.">
  <meta property="og:title" content="How Neural Rendering Redefines Look Development" />
  <meta property="og:description" content="From NeRFs to neural BRDFs—exploring production-ready applications of neural rendering in VFX workflows." />
  <meta property="og:image" content="/images/neural-rendering-hero.jpg" />
  <meta property="og:type" content="article" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  
  <style>
    :root {
      --bg:#ffffff;
      --card:#fafafa;
      --text:#1f2937;
      --muted:#6b7280;
      --accent:#1e3a8a;
      --border:#e5e7eb;
    }
    html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font:17px/1.8 system-ui,Segoe UI,Roboto,Inter,Georgia,serif}

    .article-wrap{max-width:740px;margin:0 auto;padding:60px 20px}
    .article-header{border-bottom:1px solid var(--border);padding-bottom:32px;margin-bottom:40px}
    .article-meta{display:flex;gap:16px;align-items:center;margin-bottom:20px;font-size:14px;color:var(--muted)}
    .article-tag{background:rgba(76,201,240,0.15);color:var(--accent);padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px}
    h1{margin:0 0 20px;font-size:clamp(32px,5vw,44px);line-height:1.2;letter-spacing:-0.5px}
    .article-lede{font-size:20px;color:var(--muted);line-height:1.6;margin:0}
    
    .article-content h2{font-size:28px;margin:48px 0 20px;color:var(--text);letter-spacing:-0.3px}
    .article-content h3{font-size:22px;margin:36px 0 16px;color:var(--accent)}
    .article-content p{margin:20px 0;color:var(--muted)}
    .article-content strong{color:var(--text);font-weight:600}
    .article-content a{color:var(--accent);text-decoration:none;border-bottom:1px solid transparent;transition:border-color 0.2s}
    .article-content a:hover{border-bottom-color:var(--accent)}
    
    .callout{background:var(--card);border-left:4px solid var(--accent);border-radius:8px;padding:24px 28px;margin:32px 0}
    .callout h4{margin:0 0 12px;color:var(--accent);font-size:18px;text-transform:uppercase;letter-spacing:0.5px;font-size:14px}
    .callout p{margin:8px 0}
    
    .pull-quote{font-size:24px;line-height:1.5;color:var(--accent);font-style:italic;margin:40px 0;padding:24px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);text-align:center}
    
    code{background:var(--card);color:var(--accent);padding:3px 8px;border-radius:4px;font-size:15px;font-family:Monaco,Consolas,monospace}
    
    .trajectory{background:linear-gradient(135deg, #1a1d2a 0%, #0f1115 100%);border:1px solid var(--border);border-radius:16px;padding:32px;margin:48px 0}
    .trajectory h3{margin:0 0 16px;color:var(--accent);font-size:22px}
    .trajectory p{margin:12px 0;color:var(--muted)}
    
    .article-footer{margin-top:60px;padding-top:32px;border-top:1px solid var(--border)}
    .footer-nav{display:flex;justify-content:space-between;gap:20px}
    .footer-nav a{color:var(--accent);text-decoration:none;font-size:15px}
    .footer-nav a:hover{text-decoration:underline}
    
    nav{margin:20px auto;padding:16px 0;border-bottom:1px solid var(--border);max-width:740px}
    nav a{margin-right:24px;color:var(--muted);font-size:14px;text-transform:uppercase;letter-spacing:0.5px;text-decoration:none;border:none}
    nav a:hover{color:var(--accent);text-decoration:none;border:none}
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
        <span class="article-tag">Neural Rendering</span>
        <span>12 min read</span>
        <span>Jan 2025</span>
      </div>
      <h1>How Neural Rendering Redefines Look Development</h1>
      <p class="article-lede">From NeRFs to neural BRDFs—exploring production-ready applications of neural rendering in VFX workflows.</p>
    </header>

    <div class="article-content">
      <h2>Introduction</h2>
      <p>This is the introduction section. Markdown content here.</p>

      <h3>Subsection</h3>
      <p>More markdown content with <strong>bold</strong> and <em>italic</em>.</p>

      <h2>Key Concept</h2>
      <div class="callout">
        <h4>Key Takeaway</h4>
        <p>This is a key concept that should be highlighted in a callout box.</p>
      </div>

      <h2>Conclusion</h2>
      <p>Final thoughts and forward-looking trajectory.</p>

      <div class="trajectory">
        <h3>Trajectory</h3>
        <p>Where this technology is heading and why it matters for production workflows.</p>
      </div>
    </div>

    <div class="article-footer">
      <div class="footer-nav">
        <a href="essay-previous.html">← Previous Article</a>
        <a href="essay-next.html">Next Article →</a>
      </div>
    </div>
  </article>
</body>
</html>
```

---

## GENERATOR LOGIC: Pseudocode

```python
def generate_blog_post(markdown_file_path):
    """
    Main generator function
    """
    
    # 1. Read markdown file
    with open(markdown_file_path) as f:
        content = f.read()
    
    # 2. Parse frontmatter (YAML) from markdown
    frontmatter = parse_yaml_frontmatter(content)
    markdown_body = extract_markdown_body(content)
    
    # 3. Calculate metadata
    reading_time = calculate_reading_time(markdown_body)  # words / 200
    formatted_date = format_date(frontmatter['date'])    # "Jan 2025"
    
    # 4. Convert markdown to HTML
    html_content = markdown_to_html(markdown_body)
    
    # 5. Build complete HTML page
    html_page = build_html_template({
        'title': frontmatter['title'],
        'slug': frontmatter['slug'],
        'description': frontmatter['excerpt'],
        'category': frontmatter['category'],
        'date': formatted_date,
        'reading_time': reading_time,
        'content': html_content,
        'prev_article': find_previous_article(frontmatter),
        'next_article': find_next_article(frontmatter),
        'og_image': frontmatter.get('image', '/default-og-image.jpg'),
    })
    
    # 6. Write HTML file
    output_path = f"{frontmatter['slug']}.html"
    with open(output_path, 'w') as f:
        f.write(html_page)
    
    # 7. Update index files
    update_writing_index_page(frontmatter)
    
    return output_path


def calculate_reading_time(markdown_text):
    """
    Calculate reading time: 200 words per minute
    """
    word_count = len(markdown_text.split())
    minutes = max(1, round(word_count / 200))
    return minutes


def markdown_to_html(markdown_text):
    """
    Convert markdown to HTML with special handling for:
    - Blockquotes → .callout boxes
    - Bold text → strong tags
    - Code blocks → syntax highlighting
    - Links → with proper styling
    """
    # This would use a library like python-markdown or CommonMark
    # with custom processing for callout boxes and pull quotes
    pass


def find_previous_article(current_frontmatter):
    """
    If this article is part of a series (series: "X", seriesPart: N),
    return the article with seriesPart: N-1
    
    Otherwise return the most recent article by date
    """
    pass


def build_html_template(data):
    """
    Build the complete HTML page using the template structure
    with all CSS inlined for static file deployment
    """
    pass


def update_writing_index_page(article_frontmatter):
    """
    Update writing.html to include new article in the grid:
    
    1. Read existing writing.html
    2. Parse the article card grid section
    3. Add new article card at top (most recent first)
    4. Update the grid with proper sorting by date
    5. Write back to writing.html
    """
    pass
```

---

## SPECIAL CONVERSIONS

### Blockquotes → Callout Boxes

**Markdown Input:**
```markdown
> **Key Concept**
> This is a key finding that should be highlighted
```

**HTML Output:**
```html
<div class="callout">
  <h4>Key Concept</h4>
  <p>This is a key finding that should be highlighted</p>
</div>
```

### Emphasized Quotes → Pull Quotes

**Markdown Input:**
```markdown
> *"This is a particularly important insight that deserves emphasis"*
```

**HTML Output:**
```html
<p class="pull-quote">"This is a particularly important insight that deserves emphasis"</p>
```

### Code Blocks → With Language Detection

**Markdown Input:**
````markdown
```python
import torch
model = torch.load('checkpoint.pt')
```
````

**HTML Output:**
```html
<pre><code class="language-python">import torch
model = torch.load('checkpoint.pt')</code></pre>
```

---

## ARTICLE INDEX UPDATE LOGIC

The `writing.html` file should be generated automatically by the generator:

```html
<!-- This section should be auto-generated -->
<div class="article-list">
  <!-- Article cards sorted by date (newest first) -->
  
  <a href="neural-rendering-look-development.html" class="article-card">
    <div class="article-card-header">
      <span class="article-tag">Neural Rendering</span>
      <span class="read-time">12 min read</span>
    </div>
    <h3>How Neural Rendering Redefines Look Development</h3>
    <p class="article-excerpt">From NeRFs to neural BRDFs—exploring production-ready applications of neural rendering in VFX workflows.</p>
    <div class="article-date">Jan 2025</div>
  </a>
  
  <!-- More cards... -->
</div>
```

---

## SERIES HANDLING

For articles in a series (like "Intelligent VFX Futures"), the generator should:

1. **Group by series name** in the metadata
2. **Sort by seriesPart** for navigation links
3. **Generate previous/next links** within series

**Example:**
```yaml
series: "Intelligent VFX Futures"
seriesPart: 3
```

Then:
- Previous: Part 2 (essay-predictive-pipelines.html)
- Next: Part 4 (essay-ai-co-creator.html)

---

## REQUIRED IMPLEMENTATION FEATURES

### 1. Command Line Interface
```bash
# Create new post from template
blog-generator new --title "Post Title" --category "Neural Rendering"

# Generate all posts from markdown sources
blog-generator build

# Generate single post
blog-generator build --source content/essays/sample.md

# Update index pages
blog-generator index

# Validate all posts
blog-generator validate
```

### 2. Configuration File
```yaml
# blog-generator.config.yml

site_title: "Next Wave Intelligence"
site_url: "https://michaelpistorio.com"
author: "Michael Pistorio"

content_dirs:
  essays: "content/essays"
  projects: "content/projects"
  tutorials: "content/tutorials"

output_dir: "."

metadata_schema:
  required: [title, slug, date, category, excerpt]
  optional: [image, series, seriesPart, featured, tags]

markdown_processor:
  library: "python-markdown"
  extensions: [tables, codehilite, toc]

reading_time_words_per_minute: 200
```

### 3. Post Template
```markdown
---
title: ""
slug: ""
date: "YYYY-MM-DD"
category: ""
excerpt: ""
readingTime: 
tags: []
series: ""
seriesPart: 
featured: false
image: ""
---

## Section 1

Content here.

### Subsection

More content.

> **Key Finding**
> This will become a callout box

> *"Important quote that deserves emphasis"*

This will become a pull quote.

## Conclusion

Final thoughts.
```

---

## METADATA SCHEMA

The generator should enforce this schema:

```yaml
# REQUIRED
title: string              # Article headline
slug: string               # URL slug (auto-generated from title if not provided)
date: ISO date string      # Publication date (2025-01-15)
category: string           # Article category (e.g., "Introduction", "Part 1 - CV")
excerpt: string            # Brief description for cards

# OPTIONAL
readingTime: integer       # Minutes (auto-calculated if not provided)
tags: array                # [tag1, tag2, tag3]
series: string             # Series name (e.g., "Intelligent VFX Futures")
seriesPart: integer        # Order within series
featured: boolean          # Show on homepage
image: string              # Hero image path
```

---

## VALIDATION RULES

The generator should validate:

1. **All required fields present** in frontmatter
2. **Date is ISO format** (YYYY-MM-DD)
3. **Slug is URL-safe** (lowercase, hyphens only)
4. **Category matches known categories** (or allow new ones)
5. **No duplicate slugs** across all posts
6. **Links point to existing files** (or external URLs)
7. **Images exist at specified paths**
8. **If series, seriesPart is unique** within that series

---

## DEPLOYMENT CONSIDERATIONS

Since this deploys to **GitHub Pages (static HTML)**:

1. **Generate all HTML files** before committing
2. **Keep markdown sources** in git (for editing)
3. **Commit generated HTML files** to repo
4. **CSS must be inline** (no external stylesheets)
5. **URLs must be relative** (for GitHub Pages subdirectory support if needed)
6. **Generate sitemaps** for SEO
7. **Generate RSS feed** for subscriptions

---

## NEXT STEPS

To build this generator, you'll need to:

1. Choose a technology stack (Python, Node.js, etc.)
2. Implement markdown → HTML conversion
3. Create CLI for post creation/management
4. Implement index page generation
5. Add RSS feed generation
6. Set up watch mode for development
7. Create CI/CD pipeline to auto-generate on git push

See the detailed implementation notes in `WEBSITE_STRUCTURE_ANALYSIS.md` for more context.

# Blog Post Generator - Quick Reference

## TL;DR

**Current State:**
- Static HTML website (No CMS)
- 6 essays in root directory
- Manually created HTML files
- No automation

**What's Needed:**
- Blog post generator (Markdown → HTML)
- Automation for index pages
- CLI tools for creating posts
- RSS feed generation

---

## Key Files to Reference

### For HTML Structure
- **Template:** `/home/user/michaelpistorio/essay-ai-co-creator.html`
- **Complete Example:** `/home/user/michaelpistorio/essay-neural-rendering.html`

### For Blog Listing
- **Current Index:** `/home/user/michaelpistorio/writing.html`
- **Template Example:** `/home/user/michaelpistorio/examples/blog-index.html`

### For Strategy & Planning
- **Content Strategy:** `/home/user/michaelpistorio/examples/claude web design files/vfx-ai-website-strategy.md`
- **Build Instructions:** `/home/user/michaelpistorio/examples/claude web design files/CLAUDE_CODE_INSTRUCTIONS.md`

---

## Current Blog Post List

**Root Directory Essays (Published):**
1. `essay-introduction.html` - Introduction
2. `essay-computer-vision.html` - Part 1 - Computer Vision
3. `essay-predictive-pipelines.html` - Part 2 - Prediction
4. `essay-neural-rendering-series.html` - Part 3 - Representation
5. `essay-ai-co-creator.html` - Part 4 - Platform
6. `essay-neural-rendering.html` - Bonus: How Neural Rendering Redefines Look Development

**Series:** "Intelligent VFX Futures" (5-part progression)

---

## Design System (Copy-Paste)

```css
Color Variables:
--primary-blue: #1e3a8a
--accent-cyan: #06b6d4
--accent-amber: #f59e0b
--bg-white: #ffffff
--bg-gray: #fafafa
--bg-dark: #1f2937
--text-dark: #1f2937
--text-gray: #6b7280
--border-color: #e5e7eb

Typography:
Font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
Code Font: Monaco, Consolas, monospace
Body Size: 17px
Line Height: 1.8
Max Content Width: 740px
```

---

## HTML Blog Post Template (Minimal)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>[TITLE] | Michael Pistorio</title>
  <meta name="description" content="[EXCERPT]">
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
    .callout{background:var(--card);border-left:4px solid var(--accent);border-radius:8px;padding:24px 28px;margin:32px 0}
    .callout h4{margin:0 0 12px;color:var(--accent);font-size:14px;text-transform:uppercase;letter-spacing:0.5px}
    .pull-quote{font-size:24px;line-height:1.5;color:var(--accent);font-style:italic;margin:40px 0;padding:24px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);text-align:center}
    .trajectory{background:linear-gradient(135deg, #1a1d2a 0%, #0f1115 100%);border:1px solid var(--border);border-radius:16px;padding:32px;margin:48px 0}
    .trajectory h3{margin:0 0 16px;color:var(--accent);font-size:22px}
    .article-footer{margin-top:60px;padding-top:32px;border-top:1px solid var(--border)}
    .footer-nav{display:flex;justify-content:space-between;gap:20px}
    .footer-nav a{color:var(--accent);text-decoration:none;font-size:15px}
    nav{margin:20px auto;padding:16px 0;border-bottom:1px solid var(--border);max-width:740px}
    nav a{margin-right:24px;color:var(--muted);font-size:14px;text-transform:uppercase;letter-spacing:0.5px;text-decoration:none}
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
        <span class="article-tag">[CATEGORY]</span>
        <span>[X] min read</span>
        <span>[Month Year]</span>
      </div>
      <h1>[TITLE]</h1>
      <p class="article-lede">[EXCERPT]</p>
    </header>

    <div class="article-content">
      [CONTENT]
    </div>

    <div class="article-footer">
      <div class="footer-nav">
        <a href="[PREV].html">← Previous</a>
        <a href="[NEXT].html">Next →</a>
      </div>
    </div>
  </article>
</body>
</html>
```

---

## Metadata Schema (Frontmatter)

For markdown sources, use this schema:

```yaml
---
title: "Article Title"
slug: "article-slug"
date: "2025-01-15"
category: "Introduction"
excerpt: "Brief description for card display"
readingTime: 12
tags: ["ai", "vfx"]
series: "Intelligent VFX Futures"
seriesPart: 3
featured: false
image: "/images/hero.jpg"
---

## Content starts here
```

---

## Generator Workflow

### Input (Markdown)
```
content/essays/sample.md
├─ YAML frontmatter
└─ Markdown content with special syntax
```

### Processing
1. Parse YAML frontmatter
2. Extract markdown body
3. Calculate reading time (words / 200)
4. Format date (ISO → "Jan 2025")
5. Convert markdown → HTML
6. Find previous/next articles (for series)
7. Build complete HTML file

### Output (HTML)
```
essay-slug.html
└─ Standalone, deployable file
```

### Index Update
Automatically update `writing.html` with new article card

---

## Special Content Elements

### Key Concept Box
```markdown
> **Key Finding**
> Description of the finding
```
↓ Generates ↓
```html
<div class="callout">
  <h4>Key Finding</h4>
  <p>Description of the finding</p>
</div>
```

### Pull Quote
```markdown
> *"Important insight worth emphasizing"*
```
↓ Generates ↓
```html
<p class="pull-quote">"Important insight worth emphasizing"</p>
```

### Trajectory Section
```markdown
## Trajectory

Where this is heading...
```
↓ Generates ↓
```html
<div class="trajectory">
  <h3>Trajectory</h3>
  <p>Where this is heading...</p>
</div>
```

---

## Implementation Checklist

**Phase 1: Foundation**
- [ ] Create markdown template
- [ ] Define metadata schema
- [ ] Set up project structure
- [ ] Create basic HTML template

**Phase 2: Core Generator**
- [ ] Markdown → HTML converter
- [ ] YAML frontmatter parser
- [ ] Reading time calculator
- [ ] HTML page builder

**Phase 3: Automation**
- [ ] CLI tool (new, build, validate)
- [ ] Index page generator
- [ ] Previous/next link logic
- [ ] Series handling

**Phase 4: Enhancement**
- [ ] RSS feed generator
- [ ] Social media cards
- [ ] SEO optimization
- [ ] Validation checks

**Phase 5: Deployment**
- [ ] Git hook for auto-generation
- [ ] CI/CD pipeline setup
- [ ] Deployment testing
- [ ] Documentation

---

## Recommended Tech Stack

**Option 1: Python**
- Markdown: `python-markdown` or `commonmark`
- YAML: `pyyaml`
- CLI: `click` or `typer`
- Template: `jinja2`
- RSS: `feedgen`

**Option 2: Node.js**
- Markdown: `remark` + `rehype`
- YAML: `yaml` or `js-yaml`
- CLI: `commander` or `yargs`
- Template: `ejs` or `handlebars`
- RSS: `feed`

**Option 3: Go**
- Markdown: `goldmark` or `blackfriday`
- YAML: `gopkg.in/yaml.v2`
- CLI: `cobra` or `urfave/cli`
- Template: `text/template`
- RSS: `gorss` or custom

---

## Project Structure (Proposed)

```
/home/user/michaelpistorio/
├── content/
│   ├── essays/
│   │   ├── introduction.md
│   │   ├── part-1-computer-vision.md
│   │   ├── part-2-prediction.md
│   │   ├── part-3-neural-rendering.md
│   │   ├── part-4-ai-co-creator.md
│   │   └── neural-rendering-look-development.md
│   ├── projects/
│   └── tutorials/
├── src/
│   ├── generator.py (or .js or .go)
│   ├── templates/
│   │   └── article.html
│   ├── config.yml
│   └── utils/
├── scripts/
│   ├── build.sh
│   ├── new-post.sh
│   └── validate.sh
├── [HTML output files]
├── index.html
├── writing.html
└── README.md
```

---

## Command Examples (Once Built)

```bash
# Create new post
python generator.py new --title "New Essay" --category "Research"

# Build all posts
python generator.py build

# Build single post
python generator.py build content/essays/sample.md

# Update indices
python generator.py index

# Validate posts
python generator.py validate

# Generate RSS
python generator.py rss

# Watch mode (auto-regenerate on changes)
python generator.py watch
```

---

## Documentation Files

Three comprehensive documents have been created:

1. **WEBSITE_STRUCTURE_ANALYSIS.md** (12 KB)
   - Complete breakdown of current structure
   - Technology stack details
   - Content management patterns
   - Strategic recommendations

2. **CONTENT_ARCHITECTURE.txt** (9.6 KB)
   - Visual diagrams of content relationships
   - File inventory
   - HTML template anatomy
   - Metadata patterns

3. **BLOG_GENERATOR_GUIDE.md** (15 KB)
   - Implementation guide with code examples
   - Input/output specifications
   - Generator pseudocode
   - Validation rules
   - Deployment considerations

**Plus this file: QUICK_REFERENCE.md**
   - Quick lookup for common tasks
   - Design system copy-paste
   - Template snippets
   - Implementation checklist

---

## Next Steps

1. **Choose your tech stack** (Python/Node/Go)
2. **Start with Phase 1** (foundation setup)
3. **Build the core converter** (Markdown → HTML)
4. **Implement CLI tools** (new, build)
5. **Automate index generation**
6. **Add RSS feed** (nice-to-have)
7. **Set up deployment** (GitHub Actions)

---

## Key Constraints

- Must produce valid HTML5
- CSS must be inline (static deployment)
- Must match existing design exactly
- No external dependencies in HTML files
- Support GitHub Pages deployment
- Maintain current color scheme & typography
- Support series/part organization
- Calculate reading time automatically

---

## Resources

**Markdown Tools:**
- [CommonMark Spec](https://spec.commonmark.org/)
- [python-markdown](https://python-markdown.github.io/)
- [remark](https://remark.js.org/)

**Template Engines:**
- [Jinja2](https://jinja.palletsprojects.com/)
- [EJS](https://ejs.co/)
- [Go Templates](https://golang.org/pkg/text/template/)

**Reading Time Calculation:**
- Generally 200 words per minute
- Can be customized in config

**RSS Feed Generation:**
- [Feed](https://www.npmjs.com/package/feed) (Node.js)
- [feedgen](https://github.com/lkiesow/python-feedgen) (Python)
- [gorss](https://github.com/lestrrat-go/feed) (Go)

---

**Start building! The comprehensive guides above have all the details you need.**

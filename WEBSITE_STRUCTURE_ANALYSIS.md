# Michael Pistorio Portfolio - Website Structure Analysis

## Overview

This is a **static HTML website** currently without a traditional CMS or build tool. All content pages are hand-crafted HTML files deployed to GitHub Pages.

---

## 1. FRAMEWORK & TECHNOLOGY

### Current Stack
- **Type:** Static HTML website
- **Hosting:** GitHub Pages (CNAME: michaelpistorio.com)
- **Styling:** Inline CSS (no build step)
- **Framework:** Pure HTML5 + CSS (no JS framework)
- **Build Process:** None - files are committed directly

### Design System
```css
Color Palette:
--primary-blue: #1e3a8a
--accent-cyan: #06b6d4
--accent-amber: #f59e0b
--bg-white: #ffffff
--bg-gray: #fafafa
--text-dark: #1f2937
--text-gray: #6b7280
--border-color: #e5e7eb

Typography:
Font: System UI, Segoe UI, Roboto, Inter, sans-serif
Code Font: Monaco, Consolas, monospace
Max Content Width: 740px (articles), 1400px (pages)
```

---

## 2. CURRENT BLOG POST STORAGE & STRUCTURE

### Where Content Lives
- **Location:** Root directory + `/examples` folder
- **Format:** Individual `.html` files (NOT markdown/MDX)
- **No database:** Pure static files

### Current Blog Posts & Essays
Located in root directory:
- `essay-ai-co-creator.html` (296 lines)
- `essay-computer-vision.html` (296 lines)
- `essay-introduction.html` (296 lines)
- `essay-neural-rendering.html` (377 lines)
- `essay-neural-rendering-series.html` (250 lines)
- `essay-predictive-pipelines.html` (250 lines)

### Essays in `/examples` folder
- `essay-neural-rendering.html` (template reference)

### Blog Post Template Structure
```html
<!doctype html>
<html lang="en">
<head>
  <title>[Title]</title>
  <meta name="description" content="[excerpt]">
  <style>/* Inline CSS */</style>
</head>
<body>
  <nav>
    <a href="index.html">← Back to Work</a>
    <a href="writing.html">All Writing</a>
  </nav>

  <article class="article-wrap">
    <header class="article-header">
      <div class="article-meta">
        <span class="article-tag">[CATEGORY]</span>
        <span>[X min read]</span>
        <span>[Date]</span>
      </div>
      <h1>[Title]</h1>
      <p class="article-lede">[Subtitle/Hook]</p>
    </header>

    <div class="article-content">
      <!-- Article sections with H2/H3 -->
      <!-- Callout boxes -->
      <!-- Pull quotes -->
    </div>

    <div class="article-footer">
      <div class="footer-nav">
        <a href="...">← Previous</a>
        <a href="...">Next →</a>
      </div>
    </div>
  </article>
</body>
</html>
```

### Content Organization
Essays follow a **series pattern**:
- **"Intelligent VFX Futures" Series:** 5-part progression
  - Introduction
  - Part 1 - Computer Vision
  - Part 2 - Prediction
  - Part 3 - Representation (Neural Rendering Series)
  - Part 4 - Platform (AI as Co-Creator)

---

## 3. EXISTING CONTENT MANAGEMENT INFRASTRUCTURE

### Current Content Types

**Essays/Blog Posts:**
- Stored as individual HTML files
- Each has metadata in `<article-meta>` (tag, read time, date)
- Tags: "Introduction", "Part X - [Topic]", "Neural Rendering", etc.
- Read times manually set (e.g., "12 min read")
- Dates manually set (e.g., "Jan 2025")

**Other Content Types:**
- `project-sam2.html` - SAM2 Roto Assistant project
- `project-neural-materials.html` - Neural Materials project
- `project-data-corpus.html` - Data Corpus Visualization
- `tutorial-sam2-roto.html` - Tutorial (1122 lines!)
- `note-sam2-motion-blur.html` - Research note
- `notes.html` - Notes index page
- `lab.html` - Lab/experiments page
- `writing.html` - Essays index page

**Navigation Pages:**
- `index.html` - Homepage (1023 lines)
- `tutorials.html` - Tutorials index
- `notes.html` - Notes index
- `writing.html` - Essays/Writing index

### Metadata Structure
No frontmatter/YAML - all metadata embedded in HTML:
```html
<div class="article-meta">
  <span class="article-tag">Part 4 - Platform</span>  <!-- Category -->
  <span>11 min read</span>                             <!-- Read time -->
  <span>Nov 2024</span>                                <!-- Date -->
</div>
```

---

## 4. INDEX/LISTING PAGES

**writing.html** - Essays listing with:
- Grid of article cards
- Each card shows: title, description, category tag, read time
- CSS classes:
  - `.article-list` (grid container)
  - `.article-card` (individual card)
  - `.article-tag` (category badges)

**notes.html** - Research notes listing

**tutorials.html** - Tutorials listing

**lab.html** - Lab/experiments overview

---

## 5. OVERALL PROJECT STRUCTURE

```
/home/user/michaelpistorio/
├── README.md                          # Main project README
├── index.html                         # Homepage (DataCamp-style)
├── writing.html                       # Essays index
├── notes.html                         # Notes index
├── tutorials.html                     # Tutorials index
├── lab.html                           # Lab page
├── 
├── ESSAYS (Individual HTML files)
├── essay-introduction.html
├── essay-computer-vision.html
├── essay-predictive-pipelines.html
├── essay-neural-rendering-series.html
├── essay-neural-rendering.html
├── essay-ai-co-creator.html
│
├── PROJECTS
├── project-sam2.html
├── project-neural-materials.html
├── project-data-corpus.html
│
├── TUTORIALS & NOTES
├── tutorial-sam2-roto.html
├── note-sam2-motion-blur.html
├── ai-pm-blueprint.html
├── vision-tools.html
│
├── EXAMPLE/REFERENCE FILES (in /examples)
├── examples/
│   ├── EXAMPLES_OVERVIEW.md
│   ├── PORTFOLIO_ANALYSIS.md
│   ├── README.md
│   ├── blog-index.html                # Blog template reference
│   ├── essay-neural-rendering.html    # Essay template reference
│   ├── index-enhanced.html            # Homepage option 1
│   ├── portfolio-minimal.html         # Portfolio option 2
│   ├── projects.html                  # Projects template
│   ├── research-hub.html              # Research hub template
│   │
│   └── claude web design files/
│       ├── CLAUDE_CODE_INSTRUCTIONS.md
│       ├── README.md
│       ├── vfx-ai-website-strategy.md
│       ├── vfx-ai-homepage-mockup.html
│       └── research-paper-template.html
│
├── favicon.svg
├── CNAME                              # GitHub Pages config
└── .git/                              # Git repository
```

---

## 6. CURRENT CONTENT PATTERNS

### Blog Post Patterns
**Consistent HTML structure:**
- Navigation bar with back link
- Article header with metadata (tag, read time, date)
- Main headline + lede/summary
- Content sections (H2/H3 hierarchy)
- Special elements:
  - `.callout` boxes (key concepts, findings)
  - `.pull-quote` (italic highlighted quotes)
  - `.trajectory` section (forward-looking analysis)
- Footer navigation (previous/next links)

### Tag System
Used for categorization:
- `<article-tag>` with class indicating type
- Examples: "Introduction", "Part X - [Topic]", "Neural Rendering"
- Color-coded with accent cyan (#06b6d4)

### Article Metadata
Manual tracking in HTML:
```html
<span class="article-tag">[CATEGORY]</span>
<span>[Read time] min read</span>
<span>[Month Year]</span>
```

---

## 7. WHAT'S MISSING FOR A BLOG GENERATOR

### Current Gaps
1. **No markdown source files** - Everything is hand-crafted HTML
2. **No build process** - No script to generate HTML from content
3. **No metadata system** - No centralized config for posts
4. **Manual metadata** - Read times, dates, categories all hardcoded
5. **No automation** - Creating a new post requires copying template + manual HTML editing
6. **No content listing automation** - Index pages manually list all posts
7. **No RSS feed** - No automatic feed generation
8. **No templating** - No component reuse across pages

---

## 8. STRATEGIC RECOMMENDATIONS FOR BLOG GENERATOR

### Recommended Architecture
The Claude Code instructions (`/examples/claude web design files/CLAUDE_CODE_INSTRUCTIONS.md`) suggests:

**Proposed Next.js Migration:**
```
Framework: Next.js 14+ with App Router
Styling: Tailwind CSS
Content: MDX for blog posts (markdown with React components)
Deployment: Vercel
Features needed:
  - Responsive design
  - Syntax highlighting
  - Newsletter integration
  - RSS feed generation
  - SEO optimization
  - Analytics
```

### Content Structure (Proposed)
```
/content/
├── research/          # MDX files for research papers
├── analysis/          # MDX files for analysis
└── reviews/           # MDX files for tool reviews

Frontmatter format:
---
title: "Article Title"
date: "2025-11-20"
category: "research" | "analysis" | "review"
featured: true | false
image: "/images/article-image.jpg"
excerpt: "Brief description"
author: "Michael Pistorio"
tags: ["ai", "vfx"]
readingTime: "18 min read"
---
```

---

## 9. CURRENT DESIGN EVOLUTION

Recent git commits show site redesign progression:
- **Most recent:** "Add DataCamp-style content links and navigation" (Nov 21)
- **Previous:** "Transform site into living research hub with DataCamp-style content surfaces"
- **Before that:** "Refactor homepage into research publication front page"
- **Disabled:** Dark mode (keeping white background across all pages)
- **Added:** Favicon with Next Wave Intelligence branding

The site is actively being redesigned to function as a **research publication** (like DataCamp or Distill.pub) rather than a traditional portfolio.

---

## 10. KEY FILES TO UNDERSTAND FOR BLOG GENERATOR

### Reference Templates
1. **`/examples/essay-neural-rendering.html`** - Perfect template for blog post HTML structure
2. **`essay-ai-co-creator.html`** - Actual published essay showing current format
3. **`writing.html`** - Shows how essays are listed/indexed

### Strategy Documents
1. **`/examples/claude web design files/vfx-ai-website-strategy.md`** - Full vision for content strategy
2. **`/examples/claude web design files/CLAUDE_CODE_INSTRUCTIONS.md`** - Technical build guide for Next.js version
3. **`examples/README.md`** - Implementation recommendations

### Design Reference
- **`/examples/essay-neural-rendering.html`** - Best template to replicate
- **`/examples/research-hub.html`** - Potential hub page design
- **`/examples/blog-index.html`** - Potential blog listing design

---

## SUMMARY FOR BLOG POST GENERATOR

**What Needs to Be Built:**

### Phase 1: Content Abstraction
- Create markdown source files for all existing HTML essays
- Define standard frontmatter schema (title, date, category, tags, readingTime)
- Build list of all existing posts in structured format

### Phase 2: Automation Framework
- Blog post generator (markdown → HTML)
- Automatic read time calculation
- Index page generation (writing.html, etc.)
- Category/tag page generation
- RSS feed generator

### Phase 3: Publishing Tools
- CLI tool for creating new posts
- Templates for common content types
- Batch processing for existing content
- Validation checks (required fields, formatting)

### Phase 4: Enhancement
- Search functionality
- Social media cards
- Newsletter integration
- Analytics integration

**Key Design Constraints:**
- Must match existing HTML/CSS structure exactly
- Keep white background (dark mode disabled)
- Use current color palette
- Maintain article template patterns
- Support current metadata fields (category, read time, date)
- Generate compatible HTML for static GitHub Pages deployment


# VFX Intelligence Website - Claude Code Build Instructions

## Project Overview

Build a modern, responsive website for VFX/AI research and industry analysis. The site combines tech journalism (like The Verge) with academic research (like arXiv/Distill.pub) for the visual effects and AI community.

## Context Files Provided

1. `vfx-ai-homepage-mockup.html` - Complete homepage design with HTML/CSS
2. `research-paper-template.html` - Research paper page template
3. `vfx-ai-website-strategy.md` - Full content strategy and planning document

## Technical Requirements

**Framework:** Next.js 14+ with App Router
**Styling:** Tailwind CSS (extract design tokens from mockup CSS)
**Content:** MDX for blog posts (markdown with React components)
**Deployment:** Vercel
**Features:**
- Responsive design (mobile, tablet, desktop)
- Syntax highlighting for code blocks
- Newsletter integration (ConvertKit or similar)
- RSS feed generation
- SEO optimization
- Analytics (Plausible or similar)

## Design System (from mockup CSS)

```css
/* Colors */
--primary-blue: #1e3a8a
--accent-cyan: #06b6d4
--accent-amber: #f59e0b
--bg-white: #ffffff
--bg-gray: #fafafa
--bg-dark: #1f2937
--text-dark: #1f2937
--text-gray: #6b7280
--border-color: #e5e7eb
--code-bg: #1e1e1e

/* Typography */
Font Family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
Code Font: 'Fira Code' or 'JetBrains Mono'

/* Spacing */
Container Max-Width: 1400px
Content Max-Width: 800px
Section Padding: 3-4rem vertical, 2rem horizontal
```

## Site Structure

```
/
├── app/
│   ├── layout.tsx (root layout with nav/footer)
│   ├── page.tsx (homepage)
│   ├── research/
│   │   ├── page.tsx (research index)
│   │   └── [slug]/
│   │       └── page.tsx (individual research papers)
│   ├── analysis/
│   │   ├── page.tsx (analysis index)
│   │   └── [slug]/
│   │       └── page.tsx (individual analysis articles)
│   ├── reviews/
│   │   ├── page.tsx (reviews index)
│   │   └── [slug]/
│   │       └── page.tsx (individual reviews)
│   ├── resources/
│   │   └── page.tsx
│   └── about/
│       └── page.tsx
├── components/
│   ├── Navigation.tsx
│   ├── Footer.tsx
│   ├── ArticleCard.tsx
│   ├── FeaturedArticle.tsx
│   ├── CategoryTag.tsx
│   ├── NewsletterSignup.tsx
│   ├── CodeBlock.tsx (with syntax highlighting)
│   ├── Figure.tsx
│   ├── TableOfContents.tsx
│   └── Breadcrumbs.tsx
├── content/
│   ├── research/ (MDX files)
│   ├── analysis/ (MDX files)
│   └── reviews/ (MDX files)
├── lib/
│   ├── mdx.ts (MDX processing utilities)
│   └── utils.ts
├── public/
│   └── images/
└── styles/
    └── globals.css
```

## Step-by-Step Build Instructions

### Phase 1: Project Setup

1. **Initialize Next.js project**
```bash
npx create-next-app@latest vfx-intelligence --typescript --tailwind --app --no-src-dir
cd vfx-intelligence
```

2. **Install dependencies**
```bash
npm install @next/mdx @mdx-js/loader @mdx-js/react
npm install gray-matter reading-time
npm install rehype-pretty-code shiki
npm install @tailwindcss/typography
npm install lucide-react (for icons)
```

3. **Configure Tailwind**
Extract colors and design tokens from mockup CSS into `tailwind.config.ts`

### Phase 2: Core Components

**Priority order:**
1. Navigation component (sticky header)
2. Footer component
3. Layout component (wraps all pages)
4. CategoryTag component (Research/Analysis/Review tags)
5. ArticleCard component (for grid layouts)

**Reference the mockup HTML for exact styling**

### Phase 3: Homepage

Build the homepage with these sections (refer to `vfx-ai-homepage-mockup.html`):
1. Hero section with gradient background
2. Featured article section (large image + content)
3. Latest Research grid (3 columns)
4. Industry Analysis grid (3 columns)
5. Research Initiatives section (2x2 grid with stats)
6. Newsletter signup
7. Footer

**All styling should match the mockup exactly**

### Phase 4: MDX Setup

1. Configure MDX in `next.config.js`
2. Create MDX components:
   - Code blocks with syntax highlighting
   - Figures with captions
   - Tables
   - Callout boxes (key findings, citations)
   - Custom headings with anchor links

3. Create content processing utilities:
   - Parse frontmatter (title, date, category, etc.)
   - Generate reading time
   - Extract table of contents from headings

### Phase 5: Research Paper Page

Build the research paper template (refer to `research-paper-template.html`):
- Two-column layout (content + sidebar)
- Sticky table of contents
- Author info section
- Abstract box
- Paper action buttons (Download PDF, View Code, Dataset)
- Code blocks with copy buttons
- Figure components
- Results tables
- Citation box
- Related articles section
- Sidebar resources
- Metrics display

### Phase 6: Article Pages

Create templates for:
- Analysis articles (editorial style)
- Tool reviews (with scoring)
- Tutorials (step-by-step)

### Phase 7: Index Pages

Build listing pages for:
- /research (all research papers)
- /analysis (all analysis articles)
- /reviews (all tool reviews)

Each should have:
- Grid of article cards
- Filter by date/category
- Pagination

### Phase 8: Additional Pages

- About page
- Resources page
- 404 page

### Phase 9: Features

1. **Newsletter Integration**
   - Form component
   - API route for ConvertKit/Mailchimp
   - Success/error states

2. **RSS Feed**
   - Generate RSS feed from content
   - Accessible at /feed.xml

3. **SEO**
   - Meta tags for all pages
   - OpenGraph images
   - Sitemap generation

4. **Analytics**
   - Plausible or Vercel Analytics

### Phase 10: Content Migration

Create 3 sample MDX articles:
1. Research paper on shot complexity classification
2. Analysis article on AI in VFX
3. Tool review of Runway Gen-3

## Key Implementation Notes

### Homepage Featured Article Logic
- Display most recent "featured" article (frontmatter: `featured: true`)
- Fallback to most recent research paper

### Article Metadata (Frontmatter)
```yaml
---
title: "Article Title"
date: "2025-11-20"
category: "research" | "analysis" | "review"
featured: true | false
image: "/images/article-image.jpg"
excerpt: "Brief description for cards"
author: "Your Name"
readingTime: "18 min read"
tags: ["computer-vision", "production-ml"]
resources:
  code: "https://github.com/..."
  dataset: "https://..."
  pdf: "/papers/..."
---
```

### Code Block Syntax
Use `rehype-pretty-code` with Shiki for syntax highlighting
Support these languages: python, typescript, bash, json

### Responsive Breakpoints
- Mobile: < 768px (single column)
- Tablet: 768px - 1024px (2 columns)
- Desktop: > 1024px (3 columns)

### Navigation Behavior
- Sticky on scroll
- Active state for current section
- Mobile hamburger menu

## Testing Checklist

- [ ] All pages load without errors
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Code blocks have syntax highlighting
- [ ] Copy button works on code blocks
- [ ] Newsletter form submits
- [ ] Navigation active states work
- [ ] All links functional
- [ ] Images load properly
- [ ] RSS feed generates
- [ ] SEO meta tags present
- [ ] Build completes without warnings

## Deployment

1. Connect GitHub repo to Vercel
2. Configure environment variables (newsletter API keys)
3. Set up custom domain
4. Enable analytics

## Sample Content to Create

Use the strategy document for content ideas. Create at least:
1. One research paper (shot complexity classification)
2. One analysis article (state of AI in VFX)
3. One tool review (Runway Gen-3)

## Reference Materials

The mockup files show exact styling, layouts, and components needed. Follow them closely for:
- Color schemes
- Typography
- Spacing
- Component structure
- Responsive behavior

## Questions to Ask if Needed

- Preferred newsletter service (ConvertKit, Mailchimp, Buttondown)?
- Custom domain name?
- Analytics preference?
- Any additional features?

## Success Criteria

The final website should:
1. Match the mockup designs exactly
2. Be fully responsive
3. Load quickly (Lighthouse score > 90)
4. Have working MDX blog functionality
5. Include 3 sample articles
6. Be deployable to Vercel
7. Have newsletter signup working

## Timeline Estimate

- Phase 1-3: 2-3 hours (setup + core components)
- Phase 4-5: 2-3 hours (MDX + research template)
- Phase 6-7: 1-2 hours (other templates)
- Phase 8-9: 1-2 hours (pages + features)
- Phase 10: 1 hour (sample content)

**Total: 7-11 hours for complete build**

## Getting Started Command

```bash
# Start here
npx create-next-app@latest vfx-intelligence --typescript --tailwind --app

# Then refer to Phase 2 for next steps
```

---

**Note to Claude Code:** All design specifications are in the HTML mockup files. Extract the CSS and convert to Tailwind classes. The mockups are production-ready designs that should be replicated exactly in the Next.js implementation.

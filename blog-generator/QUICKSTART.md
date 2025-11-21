# Quick Start - 5 Minutes to Your First Blog Post

## 1. Setup (2 minutes)

```bash
cd blog-generator

# Install dependencies
pip install -r requirements.txt

# Or use the setup script
bash setup.sh
```

## 2. Add API Key (1 minute)

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Get your key from: https://console.anthropic.com/

## 3. Generate Your First Post (2 minutes)

Try with the sample content:

```bash
python generate.py generate examples/sample-text.txt
```

The tool will:
1. ✅ Extract content
2. 🤖 Generate blog post with AI
3. 📝 Let you review and edit
4. 💾 Save HTML + Markdown

## 4. Review Output

The tool creates:
- `essay-[title-slug].html` - Ready to publish
- `essay-[title-slug].md` - Markdown source

Open the HTML in your browser to preview!

## Real-World Examples

### From a PDF
```bash
python generate.py generate research-paper.pdf
```

### From a URL
```bash
python generate.py generate "https://example.com/article"
```

### From a Screenshot
```bash
python generate.py generate reddit-screenshot.png
```

### With Custom Instructions
```bash
python generate.py generate input.pdf \
  --prompt "Make it beginner-friendly with lots of examples" \
  --category "Tutorial"
```

## Interactive Editing

After generation, you can:
- **continue** - Save and finish
- **refine** - Ask AI to improve specific parts
- **edit-title** - Change the title
- **preview** - See full content

Example:
```
What would you like to do? refine
What would you like to change? Add more practical examples

[AI refines...]
✓ Content refined

What would you like to do? continue
🎉 Success!
```

## Next Steps

1. Try with your own content
2. Read `README.md` for all features
3. Customize `config.yaml` for your preferences
4. Check out examples in `examples/` folder

## Troubleshooting

**API key not working?**
- Make sure it starts with `sk-ant-`
- Check it's in `.env` file (not `.env.example`)

**Dependencies failing?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Need help?**
```bash
python generate.py --help
python generate.py check  # System diagnostics
```

---

**That's it! You're ready to generate blog posts.** 🚀

Start with: `python generate.py generate examples/sample-text.txt`

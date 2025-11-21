# Example Inputs

This folder contains sample inputs you can use to test the blog post generator.

## Quick Test

Try generating a post from the sample text:

```bash
python ../generate.py generate sample-text.txt
```

Or from the transcript:

```bash
python ../generate.py generate sample-transcript.txt
```

## Testing Different Input Types

### Text Files
- `sample-text.txt` - Essay-style content
- `sample-transcript.txt` - Interview format

### URLs
Try any of these:
```bash
python ../generate.py generate "https://en.wikipedia.org/wiki/Neural_rendering"
python ../generate.py generate "https://paperswithcode.com/task/novel-view-synthesis"
```

### Your Own Content

1. **PDF**: Drop any PDF file in this folder and run:
   ```bash
   python ../generate.py generate your-paper.pdf
   ```

2. **Screenshot**: Take a screenshot of interesting content (Reddit thread, tweet, article) and save as `screenshot.png`:
   ```bash
   python ../generate.py generate screenshot.png
   ```

3. **Your Notes**: Create a `.txt` file with your ideas and generate:
   ```bash
   python ../generate.py generate my-ideas.txt
   ```

## Expected Output

Each command will:
1. Extract content from your input
2. Generate a blog post with Claude AI
3. Let you review and refine interactively
4. Output both HTML and Markdown files

The generated files will be saved in the parent directory (blog-generator/).

## Tips

- Add `--prompt "your instructions"` to guide the AI
- Use `--category "Tutorial"` to set the post type
- Try `--no-edit` for quick testing without interaction
- Run `python ../generate.py --help` to see all options

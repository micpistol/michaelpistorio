#!/usr/bin/env python3
"""
Blog Post Generator CLI
One-command blog post generation from any input type
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import yaml
import click
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from input_processor import InputProcessor
from ai_generator import AIGenerator
from html_generator import HTMLGenerator

# Load environment variables
load_dotenv()

# Rich console for pretty output
console = Console()


def load_config():
    """Load configuration"""
    config_path = Path(__file__).parent / 'config.yaml'
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@click.group()
def cli():
    """Blog Post Generator - Turn any content into beautiful blog posts"""
    pass


@cli.command()
@click.argument('input_path')
@click.option('--prompt', '-p', help='Additional instructions for the AI')
@click.option('--title', '-t', help='Override auto-detected title')
@click.option('--category', '-c', help='Blog post category')
@click.option('--output', '-o', help='Output file path (default: auto-generated)')
@click.option('--no-edit', is_flag=True, help='Skip interactive editing')
def generate(input_path, prompt, title, category, output, no_edit):
    """
    Generate a blog post from any input

    Examples:
        generate paper.pdf
        generate https://example.com/article
        generate screenshot.png
        generate transcript.txt --prompt "Focus on the key technical insights"
    """

    try:
        config = load_config()

        # Step 1: Process input
        console.print("\n[bold cyan]Step 1:[/] Processing input...", style="bold")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Reading and extracting content...", total=None)

            processor = InputProcessor(config)
            processed = processor.process(input_path)

            progress.update(task, description="✓ Content extracted successfully")

        # Show extracted info
        console.print(Panel(
            f"[bold]Source Type:[/] {processed['source_type']}\n"
            f"[bold]Detected Title:[/] {processed['title'] or 'None'}\n"
            f"[bold]Content Length:[/] {len(processed['content'])} characters",
            title="📄 Extracted Content",
            border_style="green"
        ))

        # Step 2: Generate blog post
        console.print("\n[bold cyan]Step 2:[/] Generating blog post with AI...", style="bold")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Claude is writing your blog post...", total=None)

            generator = AIGenerator(config)
            blog_post = generator.generate_blog_post(
                content=processed['content'],
                source_type=processed['source_type'],
                metadata=processed['metadata'],
                user_prompt=prompt,
                suggested_title=title or processed['title']
            )

            progress.update(task, description="✓ Blog post generated")

        # Show generated metadata
        console.print(Panel(
            f"[bold]Title:[/] {blog_post['title']}\n"
            f"[bold]Category:[/] {blog_post['category']}\n"
            f"[bold]Tags:[/] {', '.join(blog_post['tags'])}\n"
            f"[bold]Excerpt:[/] {blog_post['excerpt']}",
            title="📝 Generated Blog Post",
            border_style="green"
        ))

        # Step 3: Interactive editing (unless --no-edit)
        if not no_edit:
            console.print("\n[bold cyan]Step 3:[/] Review and edit", style="bold")

            # Show preview
            console.print("\n[dim]─── Content Preview ───[/]")
            preview = blog_post['content'][:500] + "..." if len(blog_post['content']) > 500 else blog_post['content']
            console.print(Markdown(preview))
            console.print("[dim]─────────────────────[/]\n")

            # Interactive menu
            while True:
                choice = Prompt.ask(
                    "What would you like to do?",
                    choices=["continue", "edit-title", "edit-category", "refine", "preview", "quit"],
                    default="continue"
                )

                if choice == "continue":
                    break
                elif choice == "edit-title":
                    new_title = Prompt.ask("Enter new title", default=blog_post['title'])
                    blog_post['title'] = new_title
                    console.print("[green]✓ Title updated[/]")
                elif choice == "edit-category":
                    new_category = Prompt.ask(
                        "Enter category",
                        choices=["Introduction", "Research", "Tutorial", "Analysis", "Vision"],
                        default=blog_post['category']
                    )
                    blog_post['category'] = new_category
                    console.print("[green]✓ Category updated[/]")
                elif choice == "refine":
                    feedback = Prompt.ask("What would you like to change?")
                    console.print("[dim]Refining with Claude...[/]")
                    blog_post['content'] = generator.refine_post(blog_post['content'], feedback)
                    console.print("[green]✓ Content refined[/]")
                elif choice == "preview":
                    console.print("\n[bold]Full Content:[/]")
                    console.print(Markdown(blog_post['content']))
                    console.print()
                elif choice == "quit":
                    console.print("[yellow]Cancelled[/]")
                    return

        # Step 4: Generate HTML
        console.print("\n[bold cyan]Step 4:[/] Generating HTML...", style="bold")

        # Override category if provided
        if category:
            blog_post['category'] = category

        html_gen = HTMLGenerator(config)
        html = html_gen.generate_html(
            title=blog_post['title'],
            content=blog_post['content'],
            excerpt=blog_post['excerpt'],
            category=blog_post['category'],
            date=datetime.now().strftime('%Y-%m-%d')
        )

        # Determine output path
        if not output:
            slug = html_gen._slugify(blog_post['title'])
            output = f"essay-{slug}.html"

        output_path = Path(output)

        # Save HTML
        html_gen.save_html(html, str(output_path))

        # Also save markdown version
        md_path = output_path.with_suffix('.md')
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"""---
title: {blog_post['title']}
category: {blog_post['category']}
excerpt: {blog_post['excerpt']}
tags: {', '.join(blog_post['tags'])}
date: {datetime.now().strftime('%Y-%m-%d')}
---

{blog_post['content']}
""")

        console.print(Panel(
            f"[bold green]✓ Blog post generated successfully![/]\n\n"
            f"[bold]HTML:[/] {output_path.absolute()}\n"
            f"[bold]Markdown:[/] {md_path.absolute()}\n\n"
            f"[dim]Next steps:[/]\n"
            f"1. Review the HTML in your browser\n"
            f"2. Copy to your site directory when ready\n"
            f"3. Update writing.html index",
            title="🎉 Success",
            border_style="green"
        ))

    except Exception as e:
        console.print(f"\n[bold red]Error:[/] {str(e)}", style="bold red")
        console.print("\n[dim]Troubleshooting:[/]")
        console.print("• Make sure ANTHROPIC_API_KEY is set in .env")
        console.print("• Check that all dependencies are installed: pip install -r requirements.txt")
        console.print("• For PDF/image processing, ensure system dependencies are installed")
        sys.exit(1)


@cli.command()
@click.argument('markdown_file')
@click.option('--output', '-o', help='Output HTML file')
def convert(markdown_file, output):
    """Convert existing markdown file to HTML"""

    try:
        config = load_config()

        # Read markdown file
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                markdown_content = parts[2].strip()
            else:
                frontmatter = {}
                markdown_content = content
        else:
            frontmatter = {}
            markdown_content = content

        # Generate HTML
        html_gen = HTMLGenerator(config)
        html = html_gen.generate_html(
            title=frontmatter.get('title', 'Untitled'),
            content=markdown_content,
            excerpt=frontmatter.get('excerpt', ''),
            category=frontmatter.get('category', 'Research'),
            date=frontmatter.get('date')
        )

        # Save
        if not output:
            output = Path(markdown_file).with_suffix('.html')

        html_gen.save_html(html, output)

        console.print(f"[green]✓ Converted to {output}[/]")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/]")
        sys.exit(1)


@cli.command()
def check():
    """Check if everything is set up correctly"""

    console.print("\n[bold]Checking Blog Post Generator setup...[/]\n")

    # Check Python version
    py_version = sys.version_info
    if py_version >= (3, 8):
        console.print(f"[green]✓[/] Python {py_version.major}.{py_version.minor}")
    else:
        console.print(f"[red]✗[/] Python version too old (need 3.8+)")

    # Check config
    try:
        config = load_config()
        console.print("[green]✓[/] Configuration loaded")
    except Exception as e:
        console.print(f"[red]✗[/] Config error: {e}")

    # Check API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if api_key:
        console.print("[green]✓[/] ANTHROPIC_API_KEY found")
    else:
        console.print("[red]✗[/] ANTHROPIC_API_KEY not set")
        console.print("   [dim]Create a .env file with: ANTHROPIC_API_KEY=your_key[/]")

    # Check dependencies
    try:
        import anthropic
        console.print("[green]✓[/] anthropic package installed")
    except ImportError:
        console.print("[red]✗[/] anthropic package missing")

    try:
        import requests
        console.print("[green]✓[/] requests package installed")
    except ImportError:
        console.print("[red]✗[/] requests package missing")

    try:
        from bs4 import BeautifulSoup
        console.print("[green]✓[/] beautifulsoup4 package installed")
    except ImportError:
        console.print("[red]✗[/] beautifulsoup4 package missing")

    try:
        import PyPDF2
        console.print("[green]✓[/] PyPDF2 package installed")
    except ImportError:
        console.print("[red]✗[/] PyPDF2 package missing")

    console.print("\n[bold]Run 'pip install -r requirements.txt' to install missing packages[/]\n")


if __name__ == '__main__':
    cli()

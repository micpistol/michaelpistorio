#!/bin/bash
# Blog Post Generator Setup Script

echo "🚀 Setting up Blog Post Generator..."
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found"
echo ""

# Create virtual environment (optional but recommended)
read -p "Create a virtual environment? (recommended) [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ Virtual environment created and activated"
    echo ""
fi

# Install dependencies
echo "Installing Python packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your ANTHROPIC_API_KEY"
    echo ""
    read -p "Do you want to add your API key now? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your Anthropic API key: " api_key
        sed -i.bak "s/your_api_key_here/$api_key/" .env
        rm .env.bak 2>/dev/null
        echo "✓ API key saved"
    else
        echo "Remember to edit .env before using the generator!"
    fi
else
    echo "✓ .env file already exists"
fi

echo ""

# Check for optional dependencies
echo "Checking optional dependencies..."

# Check for tesseract (for OCR)
if command -v tesseract &> /dev/null; then
    echo "✓ Tesseract OCR found (image processing enabled)"
else
    echo "⚠️  Tesseract OCR not found (image processing will not work)"
    echo "   Install with:"
    echo "   - macOS: brew install tesseract"
    echo "   - Ubuntu: sudo apt-get install tesseract-ocr"
fi

echo ""

# Run check command
echo "Running system check..."
python generate.py check

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Make sure your ANTHROPIC_API_KEY is set in .env"
echo "2. Try generating a post: python generate.py generate examples/sample-text.txt"
echo "3. Read the README.md for more examples and options"
echo ""
echo "Need help? Run: python generate.py --help"
echo ""

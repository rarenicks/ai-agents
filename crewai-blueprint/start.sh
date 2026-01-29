#!/bin/bash

# Configuration
VENV_DIR="venv"
PYTHON_BIN="$VENV_DIR/bin/python"

echo "🚀 Initializing CrewAI Production Blueprint..."

# Check for uv (high-performance python package manager)
if command -v uv &> /dev/null
then
    echo "✅ Found 'uv'. Using it for faster setup."
    uv venv $VENV_DIR
    source $VENV_DIR/bin/activate
    uv pip install -r requirements.txt
else
    echo "⚠️ 'uv' not found. Falling back to standard pip."
    python3 -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
fi

echo ""
echo "✨ Setup complete!"
echo "------------------------------------------------"
echo "To activate the environment: source venv/bin/activate"
echo "To run the crew: python src/main.py"
echo "To run the API: uvicorn api.main:app --reload"
echo "------------------------------------------------"

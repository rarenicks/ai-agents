#!/bin/bash

# Configuration
VENV_DIR="venv"
REQS_FILE="requirements.txt"
ENV_FILE=".env"

echo "🚀 Initializing LangGraph Blueprint..."

# Check for Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Error: python3 is not installed."
    exit 1
fi

# Create Virtual Environment
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate Virtual Environment
source $VENV_DIR/bin/activate

# Install Dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r $REQS_FILE

# Create .env if it doesn't exist
if [ ! -f "$ENV_FILE" ]; then
    echo "📝 Creating .env file..."
    cat <<EOT >> $ENV_FILE
OPENAI_API_KEY=your_key_here
OPENAI_MODEL_NAME=gpt-4o-mini

# LangSmith Observability
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_PROJECT=langgraph-blueprint
EOT
fi

echo "✨ Setup complete!"
echo "------------------------------------------------"
echo "To activate: source venv/bin/activate"
echo "To run API: uvicorn api.main:app --port 8005 --reload"
echo "------------------------------------------------"

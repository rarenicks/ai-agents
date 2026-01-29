#!/bin/bash

# Semantic Kernel Blueprint Setup Script
echo "🔮 Initializing Semantic Kernel Production Blueprint..."

# 1. Setup Virtual Environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Install Dependencies
echo "Installing dependencies..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# 3. Initialize .env if missing
if [ ! -f ".env" ]; then
    echo "Creating .env tracker..."
    cat <<EOT >> .env
# Model Provider: ollama, openai, azure_openai (DEFAULT: openai)
MODEL_PROVIDER=openai

# Ollama Settings
OLLAMA_MODEL_ID=llama3.2
OLLAMA_ENDPOINT=http://localhost:11434/v1

# OpenAI Settings (Get from root .env if not set)
OPENAI_MODEL_ID=gpt-4o-mini
OPENAI_API_KEY=

# Azure OpenAI Settings
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
EOT
fi

echo "✅ Setup Complete!"
echo "To run the blueprint:"
echo "1. Configure your .env file"
echo "2. Run: venv/bin/python src/main.py"

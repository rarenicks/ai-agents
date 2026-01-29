#!/bin/bash

# Configuration
VENV_DIR="venv"
REQS_FILE="requirements.txt"
ENV_FILE=".env"

echo "🚀 Initializing OpenAI Agents Blueprint..."

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
MODEL_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL_NAME=gpt-4o

# Azure OpenAI Settings (Optional)
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
EOT
fi

echo "✨ Setup complete!"
echo "------------------------------------------------"
echo "To activate: source venv/bin/activate"
echo "To run API: uvicorn api.main:app --port 8003 --reload"
echo "To deploy: ./scripts/deploy_azure.sh"
echo "------------------------------------------------"

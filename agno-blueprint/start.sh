#!/bin/bash

# Agno Production Blueprint Setup Script

# 1. Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate virtual environment
source venv/bin/activate

# 3. Upgrade pip and install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOL
OPENAI_API_KEY=
OPENAI_MODEL_NAME=gpt-4o-mini
EOL
    echo "Please update .env with your API keys."
fi

echo "Setup complete!"
echo "To run the API server:"
echo "export PYTHONPATH=\$PYTHONPATH:\$(pwd) && python api/main.py"
echo ""
echo "To run the Agent UI:"
echo "export PYTHONPATH=\$PYTHONPATH:\$(pwd) && streamlit run ui/app.py"

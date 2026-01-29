#!/bin/bash

# DSPy Blueprint Setup Script

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOL
OPENAI_API_KEY=
OPENAI_MODEL_NAME=gpt-4o-mini
EOL
    echo "Please update .env with your API keys."
fi

echo "Setup complete!"
echo "To run tests:"
echo "source venv/bin/activate && python test_dspy.py"

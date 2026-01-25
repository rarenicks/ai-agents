#!/bin/bash
echo "Starting Google AI Agent System..."
echo "Ensure you have set your credentials in .env"

# Check if .env exists
if [ ! -f .env ]; then
    echo "Warning: .env file not found. Copying .env.example to .env..."
    cp .env.example .env
    echo "Please edit .env with your actual API keys."
fi

# Run the uvicorn server
./venv/bin/uvicorn engine.main:app --host 0.0.0.0 --port 8000 --reload

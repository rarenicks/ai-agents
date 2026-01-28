# Agno Production Blueprint

This blueprint demonstrates how to build a production-ready AI agent using **Agno** (formerly Phidata). It features tool calling (DuckDuckGo), persistent session storage (SQLite), a FastAPI interface, and a **Streamlit UI**.

## Features
- **Agno Agent**: Uses the latest Agno patterns for building memory-enabled agents.
- **Tool Integration**: DuckDuckGo search for real-time information.
- **Persistence**: SQLite-based memory to persist agent sessions across restarts.
- **Production API**: FastAPI endpoints for `/chat` and `/health`.
- **Interactive UI**: Streamlit-based chat interface for easy testing and demo.
- **Configuration**: Pydantic Settings for environment variable management.
- **Optimized Prompts**: System instructions tailored for concise, one-line answers to reduce token costs.

## Architecture
- `src/agents/assistant.py`: Agent definition and tool configuration.
- `api/main.py`: FastAPI server implementation.
- `ui/app.py`: Streamlit chat interface.
- `config/settings.py`: Environment configuration.
- `agno.db`: Local SQLite database for persistent storage (auto-generated).

## Getting Started

1. **Setup Environment**:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

2. **Run the API Server**:
   ```bash
   source venv/bin/activate
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   python api/main.py
   ```

3. **Run the UI**:
   ```bash
   source venv/bin/activate
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   streamlit run ui/app.py
   ```

4. **Test the Agent Script**:
   ```bash
   source venv/bin/activate
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   python test_agno.py
   ```

## Example Usage

### Send a Chat Request (API)
```bash
curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is the latest news about AI?"}'
```

## Production Considerations
- **Database**: Switch `SqliteDb` to a production database like PostgreSQL or MySQL for scalability.
- **Security**: Implement API authentication (e.g., JWT) for the FastAPI endpoints.
- **Monitoring**: Integrate with monitoring tools.
- **Storage**: Use Agno's `Db` classes to persist more than just chat history (e.g., user profiles).

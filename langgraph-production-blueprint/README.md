# LangGraph Production Blueprint 🕸️

This blueprint demonstrates a production-grade implementation of **LangGraph**, focusing on stateful, multi-agent cyclic workflows.

## 🏗 Architecture
- **`src/state/`**: Typed schemas for the graph state.
- **`src/agents/`**: Compiled state graphs with node and edge logic.
- **`api/`**: FastAPI implementation for serving the graph.
- **`config/`**: Environment-driven settings.

## 🌟 Key Features
- **Cyclic Workflows**: Researcher -> Critic -> Researcher loop with terminal conditions.
- **Persistence**: SQLite-based context management (Checkpointing) for long-running threads.
- **LangSmith Ready**: Native integration with LangSmith for deep observability of the graph execution.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd langgraph-production-blueprint
   chmod +x start.sh
   ./start.sh
   ```

2. **Run API**:
   ```bash
   venv/bin/uvicorn api.main:app --port 8005 --reload
   ```

3. **Interact**:
   Use `curl` to send a research request:
   ```bash
   curl -X POST http://localhost:8005/research \
        -H "Content-Type: application/json" \
        -d '{"query": "The future of quantum computing"}'
   ```

## 🔍 Observability
Enable **LangSmith** by adding your token to `.env`:
```env
LANGSMITH_API_KEY=your_token_here
```
 Traces will appear in your LangSmith project automatically.

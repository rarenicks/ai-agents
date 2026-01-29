# Agno (Phidata) Blueprint

> **The Database-First Agent Framework**

This blueprint provides a complete environment for building agents with **Agno** (formerly Phidata). Agno distinguishes itself by treating **conversation history and agent state as database records** first, making it exceptionally good for long-running, persistent agent interactions.

---

## 📚 Educational Guide: Understanding Agno

### 🧠 Core Philosophy
Most agent frameworks keep memory in RAM or simple JSON files. Agno flips this: **Storage is a first-class citizen**.
- **Agents are stateless** in code but **stateful** via the database.
- Every interaction is automatically persisted.
- You can "resume" an agent's brain just by providing a `session_id`.

### 🔑 Key Concepts in this Blueprint
1.  **The `Agent` Class**: The central orchestrator. Unlike other frameworks that might separate "Chain" and "Agent", Agno combines LLM configuration, tools, and memory into one cohesive unit.
2.  **`SqliteDb` Storage**: We use SQLite for this blueprint, but Agno's power lies in how easily this swaps to PostgreSQL (using `PgDb`). This allows your agent to have "infinite" memory scalable to millions of sessions.
3.  **Tooling (`DuckDuckGoTools`)**: Agno wraps Python functions or classes as "Tools". We demonstrate this with a web search tool, showing how the agent can autonomously decide to fetch external data.

### 🏗 Architecture Explained
```
agno-blueprint/
├── src/
│   └── agents/
│       └── assistant.py    # <--- THE BRAIN. Configures the Agent, Tools, and DB connection.
├── api/
│   └── main.py             # <--- THE INTERFACE. Exposes the agent via FastAPI for frontend apps.
├── ui/
│   └── app.py              # <--- THE DEMO. A Streamlit app to chat with your agent.
├── config/
│   └── settings.py         # <--- THE CONFIG. Centralizes keys and constants (12-factor app pattern).
├── agno.db                 # <--- THE MEMORY. Auto-generated SQLite database file.
└── start.sh                # <--- THE SETUP. One-click initialization script.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
Run the startup script to create the virtual environment and install dependencies:
```bash
chmod +x start.sh
./start.sh
```
*Note: This will prompt you to add your OpenAI API Key to the newly created `.env` file.*

### 2. 🖥 Run the Agent UI
The easiest way to learn how the agent thinks is to chat with it:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
streamlit run ui/app.py
```

### 3. 🌐 Run the API Server
For deployment, you'd run this FastAPI server:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python api/main.py
```
Test it with curl:
```bash
curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Who is the CEO of Agno AI?"}'
```

---

## 🛡 Blueprint Features Checklist

| Feature | Implemented? | Notes |
| :--- | :---: | :--- |
| **Persistence** | ✅ | Use `PgDb` (PostgreSQL) instead of SQLite for concurrency in real apps. |
| **Observability** | ❌ | Integrate Agno's `AgentOps` or OpenTelemetry. |
| **API Security** | ❌ | Add API Key validation (e.g., `X-API-Key` header) in FastAPI. |
| **Containerization**| ✅ | Ready for Docker deployment. |

## 💡 Pro Tip
In `src/agents/assistant.py`, try changing `markdown=True` to `False` and inspect the raw JSON output. You'll see how Agno structures tool calls and thoughts before rendering them!

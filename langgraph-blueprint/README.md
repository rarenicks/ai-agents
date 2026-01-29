# LangGraph Blueprint

> **The Cyclic Graph Framework for Complex State**

This blueprint demonstrates a robust agent using **LangGraph**. LangGraph is designed for heavily stateful, multi-step agent workflows where you need precise control over the "flow" of execution—loops, conditionals, and persistence.

---

## 📚 Educational Guide: Understanding LangGraph

### 🧠 Core Philosophy
Standard "DAG" (Directed Acyclic Graph) chains flow in one direction (Start -> A -> B -> End). Real agents need **loops** (Plan -> Execute -> Criticize -> Plan). LangGraph enables this by treating agent execution as a **State Machine**.
- **Nodes**: Functions that do work (e.g., "WebSearch", "WriteDraft").
- **Edges**: Rules that decide where to go next (e.g., "If error, go to Retry; else go to End").
- **State**: A shared dictionary (`AgentState`) passed between all nodes.

### 🔑 Key Concepts in this Blueprint
1.  **`StateGraph`**: The map of your agent's brain. In `src/agents/research_graph.py`, we explicitly define every possible move the agent can make.
2.  **`MemorySaver` Checkpointing**: This blueprint uses `MemorySaver` (in-memory) to pause and resume the graph. In a real DB-backed app, this allows "Time Travel"—you can rewind an agent to a previous step and try a different path!
3.  **Visual Debugging**: LangGraph integrates natively with LangSmith. We've configured trace logging so you can visually inspect the loop execution.

### 🏗 Architecture Explained
```
langgraph-blueprint/
├── src/
│   ├── agents/
│   │   └── research_graph.py  # <--- THE MAP. Defines Nodes, Edges, and the Workflow Graph.
│   └── state/
│       └── agent_state.py     # <--- THE MEMORY. Defines the schema of the shared state dict.
├── api/
│   └── main.py                # <--- THE API. Serves the graph as a REST endpoint.
├── config/
│   └── settings.py            # <--- CONFIG. Maps environment variables.
└── test_graph.py              # <--- TESTER. A script to run the graph without the API.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
Initialize the environment:
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with your `OPENAI_API_KEY` and optional `LANGSMITH_API_KEY`.*

### 2. 🧪 Test the Graph Logic
Run the graph directly to see the "Researcher -> Critic" loop in action:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_graph.py
```
*Watch the console! You'll see the agent printed "steps" as it cycles through the graph.*

### 3. 🌐 Run the API Server
Deploy the graph as a service:
```bash
python api/main.py
```

### 4. 🕵️ Observe in LangSmith (Optional)
If you set `LANGSMITH_TRACING=true` in `.env`, go to [smith.langchain.com](https://smith.langchain.com) to see your agent's cyclic trace visualization.

---

## 🛡 Blueprint Features Checklist

| Feature | Implemented? | Notes |
| :--- | :---: | :--- |
| **Persistence** | ⚠️ | Currently using `MemorySaver` (RAM). Switch to `PostgresSaver` for real apps. |
| **Async** | ✅ | The API and Graph uses `async/await` for high concurrency. |
| **Retries** | ❌ | Add node-level retry policies for robust web searching. |
| **Streaming** | ❌ | API currently waits for full response. Upgrade to SSE (Server-Sent Events) for real-time UX. |
| **Containerization**| ✅ | `Dockerfile` included. |

## 💡 Pro Tip
Open `src/state/agent_state.py`. Add a new field (e.g., `user_sentiment: str`) to the `AgentState` class. Then update `research_graph.py` to populate it. You've just permanently expanded your agent's short-term memory!

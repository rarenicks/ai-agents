# CrewAI Production Blueprint

> **The Role-Based Agent Orchestrator**

This blueprint utilizes **CrewAI**, a framework designed for orchestrating **Teams** of agents. It excels at mimicking real-world organizational structures where specialized roles (Researcher, Analyst, Writer) collaborate on a shared mission.

---

## 📚 Educational Guide: Understanding CrewAI

### 🧠 Core Philosophy
CrewAI is built around the concept of **Process Management**. You don't just "chat" with a Crew; you assign it a **Task**.
- **Agents**: Define *Who* does the work (Role, Goal, Backstory).
- **Tasks**: Define *What* needs to be done (Description, Expected Output).
- **Process**: Defines *How* they collaborate (Sequential, Hierarchical).

### 🔑 Key Concepts in this Blueprint
1.  **Config-Driven Design**: Look at `config/agents.yaml` and `config/tasks.yaml`. CrewAI allows you to separate the *logic* (Python) from the *definitions* (YAML). This makes it easy for non-engineers to tweak prompt phrasing without touching code.
2.  **Custom Tools (`TimeTools`)**: We show how to inject custom Python logic (a simple time checker) into a Crew. The agents can use these tools naturally to fulfill their goals.
3.  **FastAPI Wrapper**: CrewAI is often run as a script. This blueprint wraps the Crew in a standard API (`api/main.py`), making it ready to be triggered by a frontend or a webhook.

### 🏗 Architecture Explained
```
crewai-production-blueprint/
├── src/
│   ├── crew.py                # <--- THE TEAM. Loads YAMLs and assembles the Agents & Tasks.
│   └── tools/
│       └── custom_tool.py     # <--- THE UTILITIES. Custom python tools for the agents.
├── config/
│   ├── agents.yaml            # <--- THE ROLES. YAML definitions of your agent personas.
│   └── tasks.yaml             # <--- THE JOBS. YAML definitions of the work to be done.
├── api/
│   └── main.py                # <--- THE TRIGGER. API endpoint to "kickoff" the crew.
└── start.sh                   # <--- SETUP.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`.*

### 2. 🧪 Run the Crew Locally
Execute the crew directly to see the collaboration in your terminal:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/crew.py
```
*Watch the "Senior Researcher" find information and pass it to the "Reporting Analyst" to write the final report.*

### 3. 🌐 Run the API Server
Trigger the crew via a POST request:
```bash
python api/main.py
```
```bash
curl -X POST http://localhost:8000/kickoff \
     -H "Content-Type: application/json" \
     -d '{"topic": "The Future of Quantum Computing"}'
```

---

## 🛡 Production Readiness Checklist

| Feature | Implemented? | Production Recommendation |
| :--- | :---: | :--- |
| **Separation of Concerns** | ✅ | YAML configs isolate prompts from code. |
| **Observability** | ❌ | CrewAI has built-in tracing, but integrating `LangSmith` is recommended for deep debugging. |
| **Memory** | ⚠️ | CrewAI has short-term memory. Enable `memory=True` in `Crew(...)` for embedding-based long-term memory (requires OpenAI embeddings). |
| **Costs** | ⚠️ | Crews can be chatty. Use smaller models (e.g., `gpt-4o-mini`) for the "worker" agents and larger ones for the "manager". |

## 💡 Pro Tip
In `src/crew.py`, change `process=Process.sequential` to `process=Process.hierarchical`. This automatically adds a "Manager" agent that overrides the sequential flow and assigns tasks dynamically based on agent load and capability!

# OpenAI Agents (Swarm) Production Blueprint

> **The Native Multi-Agent SDK**

This blueprint provides a production reference for the **OpenAI Agent SDK** (often evolving from patterns like "Swarm"). It focuses on **native handoffs**—the cleanest way to coordinate multiple specialized agents.

---

## 📚 Educational Guide: Understanding Agent Handoffs

### 🧠 Core Philosophy
One giant agent is often bad at everything. "Swarm" style architectures break problems down into specialized agents (e.g., a "Triage Agent" that just routes calls, a "Sales Agent", and a "Support Agent").
The magic is in the **Handoff**: Agent A can return a `Result` that contains a pointer to Agent B. The execution loop automatically switches context to Agent B without the user noticing.

### 🔑 Key Concepts in this Blueprint
1.  **Handoff Functions**: In `src/agents/handoff_agents.py`, look at `transfer_to_flight_modification`. It's a Python function that simply returns the `flight_modification_agent`. This is the fundamental primitive of multi-agent coordination here.
2.  **The Runner Loop**: We built a custom `Runner` in `src/workflows/runner.py`. It keeps calling the current agent until the agent returns a final message or a handoff. If it returns a handoff, the loop updates `current_agent` and continues immediately.
3.  **Routine-Based Logic**: Instead of complex prompts with 50 instructions, each specialized agent has a tiny, focused system prompt. This reduces cost and hallucinations.

### 🏗 Architecture Explained
```
openai-agents-blueprint/
├── src/
│   ├── agents/
│   │   └── handoff_agents.py   # <--- THE TEAM. Defines Triage, Flight, and Hotel agents + handoff tools.
│   └── workflows/
│       └── runner.py           # <--- THE ENGINE. Manages the loop and agent switching.
├── infra/
│   └── main.bicep              # <--- THE CLOUD. Infrastructure-as-Code for Azure deployment.
├── run_demo.py                 # <--- THE DEMO. Runs a CLI conversation to show handoffs.
└── config/
    └── settings.py             # <--- CONFIG. Supports both OpenAI and Azure OpenAI.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with your Keys.*

### 2. 🧪 Experience the Handoffs
Run the interactive demo. Try asking "I want to change my flight."
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python run_demo.py
```
*Observe the console logs: You'll see `[Triage Agent] Transferring to Flight Modification Agent...`.*

### 3. ☁️ Enterprise Ready?
This blueprint includes a `main.bicep` file. If you are on Azure, you can deploy this entire architecture natively to Azure Container Apps with Azure OpenAI Service using one command.

---

## 🛡 Production Readiness Checklist

| Feature | Implemented? | Production Recommendation |
| :--- | :---: | :--- |
| **Handoffs** | ✅ | Native function-based handoffs used. |
| **State** | ❌ | Currently stateless. You need to pass a `context` dict through the runner loop for real apps. |
| **Guardrails** | ❌ | Add content filters (Azure AI Content Safety) in the runner loop. |
| **Models** | ✅ | Supports both `gpt-4o` (OpenAI) and Azure deployments via `config/settings.py`. |
| **Containerization**| ✅ | `Dockerfile` and `main.bicep` included. |

## 💡 Pro Tip
The "Handoff" pattern is extremely powerful for valid state enforcement. For example, the `flight_modification_agent` can demand a `booking_reference` before doing anything. The `triage_agent` doesn't need to know about booking references; it just hands off!

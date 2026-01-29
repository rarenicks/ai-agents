# Google AI Agent System - Enterprise Edition

> **The Enterprise ADK Platform**

Welcome to the **Google AI Agent System**, a professional-grade reference implementation for building multi-agent ecosystems. This platform leverages the **Google Agent Development Kit (ADK)** to coordinate specialized agents, manage enterprise safety, and provide deep observability.

---

## 📚 Educational Guide: Understanding Google ADK

### 🧠 Core Philosophy
Most frameworks are "toys" or "scripts". The **ADK (Agent Development Kit)** is engineered for **Systemic Reliability**.
- **Supervisor Pattern**: A central brain (Supervisor) that doesn't just "chat" but "delegates" responsibility.
- **Plugins**: Enterprise-grade interceptors that sit *between* the LLM and the Tool. This allows for logging, PII redaction, and policy enforcement *without* changing the agent code.
- **Model Context Protocol (MCP)**: Native support for connecting to remote tool servers, making this system extensible beyond a single container.

### 🔑 Key Concepts in this Blueprint
1.  **Registry Pattern**: Look at `frameworks/registry/llm_registry.py`. We don't hardcode models. We have a central registry that routes requests to Gemini, GPT-4, or even local Ollama models dynamically.
2.  **Supervisor & Delegation**: In `engine/agents/supervisor.py`, the agent doesn't do the work. It plans. It delegates to the `Researcher` or `Writer` (found in `engine/agents/*`). This separation of "Planning" and "Execution" is critical for reducing hallucinations in complex tasks.
3.  **Plugins**: The `frameworks/adk/plugins.py` file demonstrates how to inject "Guardrails". If an agent tries to execute a dangerous tool, the Plugin intercepts it before it ever runs.

### 🏗 Architecture Explained
```
google-ai-agent-system/
├── engine/
│   └── agents/               # <--- THE WORKFORCE. Supervisor, Researcher, Writer, Analyst definitions.
├── frameworks/
│   ├── adk/                  # <--- THE KERNEL. Core classes for Agents, Tools, and Plugins.
│   ├── mcp/                  # <--- EXTENSIONS. Client for connecting to remote tool servers.
│   └── registry/             # <--- THE ROUTER. Handles LLM instantiation (Gemini/Ollama/OpenAI).
├── api/
│   └── main.py               # <--- THE GATEWAY. Unified API surface.
├── docs/                     # <--- KNOWLEDGE. Deep dives into Architecture, Tools, and Ops.
└── terraform/                # <--- DEPLOYMENT. GCP Infrastructure-as-Code.
```

---

## 🚀 One-Minute Quick Start

### 1. 🛠 Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # App asks for GOOGLE_API_KEY (for Gemini) or acts in local mode
```

### 2. ⚡ Launch the Engine
```bash
./start.sh
```

### 3. 🏥 Verify Health
Run the diagnostic script to ensure agents are online and the registry is loaded:
```bash
./venv/bin/python3 scripts/system_health.py
```

### 4. 🧪 Run a CLI Demo
```bash
python run_cli.py
```

---

## 📖 Deep Dive Documentation
For a complete masterclass on building enterprise systems, read our specialized guides:
-   [**🏗 Architecture**](docs/ARCHITECTURE.md): The Supervisor Pattern & Internals.
-   [**🤝 Coordination**](docs/COORDINATION.md): How delegation works under the hood.
-   [**🛡 Plugins & Safety**](docs/PLUGINS.md): Implementing corporate policies.
-   [**🌐 Tools & MCP**](docs/TOOLS_AND_MCP.md): Hybrid local/remote tooling.

---

## 🛡 Blueprint Features Checklist

| Feature | Implemented? | Notes |
| :--- | :---: | :--- |
| **Model Agnosticism** | ✅ | Supports Gemini (Vertex/Studio), OpenAI, and Ollama via `LLMRegistry`. |
| **Safety Layers** | ✅ | Plugins system is active. Add custom PII filters for production. |
| **Infrastructure** | ✅ | Full Terraform scripts included for GCP deployment. |
| **Health Checks** | ✅ | `scripts/system_health.py` and API health endpoints are production-ready. |

## 💡 Pro Tip
Check `docs/TOOLS_AND_MCP.md`. The system leverages **MCP (Model Context Protocol)**. This means you can run a "Tool Server" on a completely different machine (e.g., a secure internal server accessing SQL) and this Agent System can "discover" and use those tools safely over the network!

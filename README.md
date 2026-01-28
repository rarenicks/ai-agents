# AI Agent Blueprint Bank 🚀

> **The "Golden Standard" Repository for Production-Grade AI Agents**

Welcome to the **AI Agent Blueprint Bank**. This repository serves as the definitive reference library for building enterprise-ready agentic systems. We have consolidated high-quality, production-hardened blueprints for every major agent framework in the ecosystem.

---

## 🧭 The Decision Matrix: Choosing Your Framework

Not all agents are created equal. Use this matrix to select the right tool for your specific problem domain.

| Framework | Best For... | Philosophy | Key "Superpower" |
| :--- | :--- | :--- | :--- |
| **[Google ADK](./google-ai-agent-system)** | **Enterprise Platforms** | System-over-Agent | 🛡 **Reliability**: RBAC, Supervision, & Observability built-in. |
| **[LangGraph](./langgraph-production-blueprint)** | **Complex Logic** | Graph Theory | 🔄 **Loops**: Cyclic state machines with time-travel logging. |
| **[CrewAI](./crewai-production-blueprint)** | **Creative Teams** | Role-Playing | 🎭 **Orchestration**: Mimics real-world org charts (Manager/Worker). |
| **[PydanticAI](./pydantic-ai-production-blueprint)** | **Production Apps** | Type Theory | 🔒 **Type Safety**: Guaranteed structured inputs/outputs via validation. |
| **[Agno (Phidata)](./agno-production-blueprint)** | **Long-Running Chat** | Database-First | 💾 **Memory**: Sessions are DB records first, code second. |
| **[LlamaIndex](./llamaindex-production-blueprint)** | **Data-Heavy Agents** | Retrieval-First | 📚 **RAG**: Best-in-class vector store and query engine integration. |
| **[OpenAI Swarm](./openai-agents-production-blueprint)** | **Native Handoffs** | Minimalist | 🤝 **Simplicity**: Zero-abstraction function routing (Agent A -> Agent B). |
| **[AutoGen](./autogen-production-blueprint)** | **Coding & Analysis** | Conversation | 📦 **Sandboxing**: Runs code safely in Docker containers. |
| **[Semantic Kernel](./semantic-kernel-production-blueprint)** | **Legacy Integration** | Plugin Architecture | 🔌 **Versatility**: Easy integration with C#/.NET and existing business logic. |

---

## 🏗 Anatomy of a Blueprint

Every blueprint in this repository follows a **Unified Architecture**, making it easy for you to switch between frameworks without relearning project layout.

> **The Standard Directory Structure**

```text
blueprint-name/
├── src/
│   ├── agents/          # <--- THE BRAIN: Agent definitions, Prompts, and Graphs.
│   ├── tools/           # <--- THE HANDS: Python functions or Class-based tools.
│   └── state/           # <--- THE MEMORY: Pydantic models for state or session logic.
├── api/
│   └── main.py          # <--- THE FACE: FastAPI server wrapping the agent.
├── config/
│   └── settings.py      # <--- THE NERVES: Environment variables (Pydantic Settings).
├── ui/                  # <--- THE DEMO: Streamlit or Chainlit app for testing.
├── tests/               # <--- THE ALARM: Pytest suite.
├── start.sh             # <--- THE KEY: One-click setup script.
└── README.md            # <--- THE MANUAL: Educational guide.
```

---

## 🌟 Production Standards

Regardless of the framework, every blueprint adheres to these strict standards:

### 1. Environment Isolation 🔒
-   **No Dependency Hell**: Each project has its own `venv` and `requirements.txt`.
-   **Local Config**: Each project uses its own `.env` file. We do not use a global root config.

### 2. Configuration as Code ⚙️
-   We use `pydantic-settings` or `python-dotenv`.
-   No hardcoded API keys.
-   Defaults provided for non-sensitive values (models, timeouts).

### 3. API-First Design 🔌
-   Agents are not just scripts; they are **Services**.
-   Every blueprint includes a `FastAPI` (or equivalent) server.
-   Ready for Dockerization and Kubernetes deployment.

### 4. Deep Observability 🔭
-   Pre-configured hooks for **LangSmith**, **Logfire**, or **AgentOps**.
-   You can see *what* the agent is thinking, not just the final answer.

---

## 🚀 Getting Started

### Step 1: Clone & Explore
```bash
git clone https://github.com/rarenicks/ai-agents.git
cd ai-agents
```

### Step 2: Pick Your Fighter
Navigate to the framework that interests you.
```bash
cd langgraph-production-blueprint
```

### Step 3: One-Click Setup
Use our standardized startup script to initialize the environment.
```bash
chmod +x start.sh
./start.sh
```
*Follow the prompts to add your API Keys to the newly created `.env` file.*

### Step 4: Learn
Open the `README.md` in that folder. It contains a "Deep Dive" section explaining the philosophy of that specific framework.

---

## 🤝 Contributions
This is a living library. We welcome contributions that:
-   **Add new patterns** (e.g., Evaluation pipelines, new Tooling ecosystems).
-   **Update frameworks** to their latest breaking changes.
-   **Optimize infrastructure** (e.g., Terraform/Bicep template improvements).

## 📜 License
This project is licensed under the **MIT License**.

---
*Maintained by the Agentic AI Community. For questions, reach out to [ai.avdhesh@gmail.com](mailto:ai.avdhesh@gmail.com).*

# AI Agent Blueprint Bank 🚀

Welcome to the **AI Agent Blueprint Bank**. This repository is a "Golden Single Repo" for production-grade agent architectures across all major providers (Google, CrewAI, AutoGen, Semantic Kernel, etc.).

Each blueprint in this bank is designed for stability, scalability, and enterprise readiness, following best practices for configuration, observability, and deployment.

---

## 🏗 Available Blueprints

### 1. Google AI Agent System (ADK)
- **Framework**: Google Agent Development Kit (ADK)
- **Directory**: `google-ai-agent-system/`
- **Focus**: Supervisor pattern, RBAC, MCP native, Deep Observability.
- [Architecture Docs](google-ai-agent-system/docs/ARCHITECTURE.md) | [Tools Info](google-ai-agent-system/docs/TOOLS_AND_MCP.md)

### 2. CrewAI Production Blueprint
- **Framework**: CrewAI
- **Directory**: `crewai-production-blueprint/`
- **Focus**: YAML-driven config, Microservices ready (FastAPI), Custom Enterprise Tools.
- [Blueprint Overview](crewai-production-blueprint/README.md)

### 3. OpenAI Agent SDK
- **Framework**: OpenAI Agent SDK
- **Directory**: `openai-agents-production-blueprint/`
- **Focus**: The official SDK for production multi-agent systems, featuring native handoffs and deep Azure integration.
- [Blueprint Overview](openai-agents-production-blueprint/README.md)

### 4. AutoGen Production Blueprint
- **Framework**: Microsoft AutoGen
- **Directory**: `autogen-production-blueprint/`
- **Focus**: Multi-agent orchestration, sandboxed code execution, and modular state flows.
- [Blueprint Overview](autogen-production-blueprint/README.md)

### 5. PydanticAI Production Blueprint
- **Framework**: PydanticAI
- **Directory**: `pydantic-ai-production-blueprint/`
- **Focus**: Type-safe agents with structured outputs and Logfire observability.
- [Blueprint Overview](pydantic-ai-production-blueprint/README.md)

### 6. Semantic Kernel Blueprint

---

## 🚀 Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rarenicks/ai-agents.git
    cd ai-agents
    ```

2. **Deploy a Blueprint**:
    Each blueprint is a self-contained production environment. Navigate to the blueprint of your choice and follow its specific `README.md`.
    ```bash
    cd crewai-production-blueprint
    chmod +x start.sh
    ./start.sh
    ```

---

### 7. LangGraph Production Blueprint
- **Framework**: LangGraph
- **Directory**: `langgraph-production-blueprint/`
- **Focus**: Stateful, multi-agent cyclic workflows with SQLite persistence and LangSmith tracing.
- [Blueprint Overview](langgraph-production-blueprint/README.md)

---

### 8. LlamaIndex Production Blueprint
- **Framework**: LlamaIndex
- **Directory**: `llamaindex-production-blueprint/`
- **Focus**: Data-augmented agents (RAG) using the ReAct pattern for ground-truth reasoning.
- [Blueprint Overview](llamaindex-production-blueprint/README.md)

---

### 9. Agno Production Blueprint
- **Framework**: Agno (formerly Phidata)
- **Directory**: `agno-production-blueprint/`
- **Focus**: Database-first agents with persistent session storage, tool-calling, and Streamlit UI.
- [Blueprint Overview](agno-production-blueprint/README.md)

---

## 🎯 Our Mission
To provide the definitive "Golden Standard" for agentic workflows. Every blueprint here is more than just a tutorial—it's a foundation you can build your enterprise products on.

## 🤝 Contributions
We welcome contributions that add new high-tier architectures or improve the robustness of existing ones.

## 📜 License
This project is licensed under the MIT License.

---
*For support or inquiries, contact [ai.avdhesh@gmail.com](mailto:ai.avdhesh@gmail.com).*

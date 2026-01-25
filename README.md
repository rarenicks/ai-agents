# ai-agents (Enterprise Codebank)

Welcome to the **ai-agents** codebank. This repository is a curated collection of AI agent implementations, ranging from introductory tutorials to enterprise-grade autonomous systems.

## 🚀 Production Blueprints (Golden Templates)

These are our highest-tier implementations, designed for stability, scalability, and production deployment.

### 1. Google AI Agent System (ADK)
**Directory: `google-ai-agent-system/`**
- **Architecture**: Enterprise-ready multi-agent platform using Google ADK.
- **Features**: Supervisor pattern, RBAC, MCP native, Deep Observability.
- [Architecture](google-ai-agent-system/docs/ARCHITECTURE.md) | [Tools](google-ai-agent-system/docs/TOOLS_AND_MCP.md)

### 2. CrewAI Production Blueprint
**Directory: `crewai-production-blueprint/`**
- **Architecture**: YAML-driven, decorator-based CrewAI system with FastAPI.
- **Features**: YAML-first config, Microservices ready, Custom Enterprise Tools, Standardized Logging.
- [Blueprint Overview](crewai-production-blueprint/README.md)

---

## 📚 Educational Implementations

### 1. Agents From Scratch (LangGraph Workshop)
**Directory: `notebooks/`, `src/email_assistant/`**
A comprehensive guide to building agents from first principles using LangGraph.

### 2. Framework Tutorials
- **[Basic Crew AI Tutorial](basic-crew-ai-agent-tutorial)**: Introduction to multi-agent coordination.
- **[Basic LangChain Tutorial](basic-langchain-agent-tutorial)**: Fundamentals of tool-calling.

---

## 🛠 Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rarenicks/ai-agents.git
    cd ai-agents
    ```

2. **Run the Enterprise System**:
    ```bash
    cd google-ai-agent-system
    ./start.sh
    ./venv/bin/python scripts/system_health.py # Run diagnostics
    ```

---

## 🤝 Contributions
All contributions, whether adding new agents or improving existing documentation, are highly encouraged.

## 📜 License
This project is licensed under the MIT License.

---
*For support or inquiries, contact [ai.avdhesh@gmail.com](mailto:ai.avdhesh@gmail.com).*

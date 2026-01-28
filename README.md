# AI Agent Blueprint Bank 🚀

> **The "Golden Standard" Repository for Production-Grade AI Agents**

Welcome to the **AI Agent Blueprint Bank**. This repository serves as a definitive reference library for building enterprise-ready agentic systems. We have consolidated high-quality, production-hardened blueprints for every major agent framework in the ecosystem.

Each blueprint is a self-contained project with its own API, configuration management, testing suite, and educational guide.

---

## 🧭 How to Choose Your Framework

| Framework | Best Used For... | Key "Superpower" | Directory |
| :--- | :--- | :--- | :--- |
| **[Google ADK](./google-ai-agent-system)** | **Enterprise Platforms** | 🛡 **Reliability**: RBAC, Supervision, & Observability built-in. | `google-ai-agent-system/` |
| **[LangGraph](./langgraph-production-blueprint)** | **Complex Logic** | 🔄 **Loops**: Cyclic state machines with time-travel. | `langgraph-production-blueprint/` |
| **[CrewAI](./crewai-production-blueprint)** | **Role-Based Teams** | 🎭 **Orchestration**: Mimics real-world team structures. | `crewai-production-blueprint/` |
| **[PydanticAI](./pydantic-ai-production-blueprint)** | **Production Apps** | 🔒 **Type Safety**: Guaranteed structured inputs/outputs. | `pydantic-ai-production-blueprint/` |
| **[Agno (Phidata)](./agno-production-blueprint)** | **Long-Running Chat** | 💾 **Memory**: Database-first design for endless sessions. | `agno-production-blueprint/` |
| **[LlamaIndex](./llamaindex-production-blueprint)** | **Data-Heavy Agents** | 📚 **RAG**: Best-in-class retrieval integration. | `llamaindex-production-blueprint/` |
| **[OpenAI Swarm](./openai-agents-production-blueprint)** | **Native Handoffs** | 🤝 **Simplicity**: Zero-abstraction function routing. | `openai-agents-production-blueprint/` |
| **[AutoGen](./autogen-production-blueprint)** | **Coding & Analysis** | 📦 **Sandboxing**: Runs code safely in Docker containers. | `autogen-production-blueprint/` |
| **[Semantic Kernel](./semantic-kernel-production-blueprint)** | **App Integration** | 🔌 **Plugins**: Easy integration with existing business logic. | `semantic-kernel-production-blueprint/` |

---

## 🏗 Key Features Across All Blueprints

Regardless of the framework, every blueprint in this repository adheres to these **Production Standards**:

1.  **Environment Isolation**: Each project has its own `.env` and `venv`. No dependency hell.
2.  **Configuration as Code**: We use `Pydantic Settings` or `python-dotenv` to manage secrets.
3.  **API First**: Every agent is wrapped in a **FastAPI** or equivalent server, ready for deployment.
4.  **Observability**: Pre-configured hooks for tracing (LangSmith, Logfire, ADK Plugins).
5.  **Educational Guides**: Each `README.md` contains a "Deep Dive" section explaining the *Philosophy* of that specific framework.

---

## 🚀 Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/rarenicks/ai-agents.git
    cd ai-agents
    ```

2.  **Pick a Blueprint**:
    Navigate to the folder of the framework you want to learn.
    ```bash
    cd langgraph-production-blueprint
    ```

3.  **Run the Setup Script**:
    We provide a consistent startup experience.
    ```bash
    chmod +x start.sh
    ./start.sh
    ```

4.  **Read the Guide**:
    Open the `README.md` in that folder for a masterclass on that specific framework.

---

## 🤝 Contributions

This is a living library. We welcome contributions that:
-   Add new enterprise patterns (e.g., Evaluation pipelines).
-   Update frameworks to their latest breaking changes.
-   Add new "Blueprints" for emerging frameworks.

## 📜 License

This project is licensed under the **MIT License**.

---
*Maintained by the Agentic AI Community. For questions, reach out to [ai.avdhesh@gmail.com](mailto:ai.avdhesh@gmail.com).*

# ai-agents (Enterprise Codebank)

Welcome to the **ai-agents** codebank. This repository is a curated collection of AI agent implementations, ranging from introductory tutorials to enterprise-grade autonomous systems.

## 🏆 Featured Project: Google AI Agent System (ADK)
**Directory: `google-ai-agent-system/`**

This is our flagship implementation of an enterprise-ready multi-agent platform using the **Google Agent Development Kit (ADK)**. 

### 🌟 Key Capabilities
- **Supervisor Pattern**: High-level orchestration between specialized Researcher and Writer agents.
- **Enterprise Safety**: Custom **ADK Plugins** for policy enforcement and safety guardrails.
- **Deep Observability**: Real-time trace logging of thoughts, tool calls, and model metadata.
- **MCP Protocol**: Native support for **Model Context Protocol** to discover and call remote enterprise tools.
- **Ops Ready**: Built-in health checks, context caching, and session resumability.

**Documentation Quick Links:**
[🏗 Architecture](google-ai-agent-system/docs/ARCHITECTURE.md) | [🛡 Plugins](google-ai-agent-system/docs/PLUGINS.md) | [🌐 Tools & MCP](google-ai-agent-system/docs/TOOLS_AND_MCP.md) | [🏥 Health & Ops](google-ai-agent-system/docs/HEALTH_AND_OPS.md)

---

## 📚 Educational Implementations

### 1. Agents From Scratch (LangGraph Workshop)
**Directory: `notebooks/`, `src/email_assistant/`**
A comprehensive guide to building agents from first principles using LangGraph, building up to an "ambient" agent that manages email via the Gmail API.

### 2. Crew AI Implementations
- **[Basic Crew AI Tutorial](basic-crew-ai-agent-tutorial)**: Introduction to task-based multi-agent coordination for content creation.

### 3. LangChain Agent Tutorials
- **[Basic LangChain Tutorial](basic-langchain-agent-tutorial)**: Learning the fundamentals of tool-calling and reasoning chains.

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

# Google AI Agent System - Enterprise Edition

Welcome to the **Google AI Agent System**, a professional-grade reference implementation for building multi-agent ecosystems. This platform leverages the **Google Agent Development Kit (ADK)** to coordinate specialized agents, manage enterprise safety, and provide deep observability.

![System Architecture](https://img.shields.io/badge/Architecture-Supervisor--Pattern-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-Google--ADK-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-All--Systems--Functional-green?style=for-the-badge)

---

## 📖 Essential Documentation

Navigate the platform with our specialized guides:

-   [**🏗 Architecture**](docs/ARCHITECTURE.md): Deep dive into the Supervisor Pattern, Registry design, and internal communication protocols.
-   [**🛡 Plugins & Safety**](docs/PLUGINS.md): Learn how ADK Plugins handle observability, trace logging, and corporate security policies.
-   [**🌐 Tools & MCP**](docs/TOOLS_AND_MCP.md): Discover the hybrid tool system combining local Python functions with remote **Model Context Protocol** services.
-   [**👤 Identity & RBAC**](docs/IDENTITY.md): Learn how the platform manages user identities and enforces permission-based access control.
-   [**🏥 Health & Ops**](docs/HEALTH_AND_OPS.md): Setup instructions for health monitoring, system diagnostics, and performance optimization.

---

## 🚀 One-Minute Quick Start

### 1. Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Update your GOOGLE_API_KEY
```

### 2. Launch the Engine
```bash
./start.sh
```

### 3. Verify Health
```bash
./venv/bin/python3 scripts/system_health.py
```

---

## 🛠 Platform Highlights

### 🧠 Strategic Orchestration
The system uses a central **Supervisor** to plan and delegate tasks. It utilizes native ADK delegation to transfer control between high-level reasoning and specialized worker agents like the **Researcher** and **Writer**.

### 🔌 Enterprise Plugin Architecture
-   **Observability**: Real-time logging of thoughts and tool executions.
-   **Guardrails**: Automated policy injection and sensitive tool intercepts.
-   **Efficiency**: Native context caching and session resumability.

### 🏢 Cross-Cloud Versatility
Whether you use **Google Gemini** (Vertex AI / AI Studio) or local models via **Ollama**, the platform adapts seamlessly using the **LiteLLM** registry integration.

---

## 🤝 Contributions
We welcome contributions to the agent registry, tool implementations, and core engine enhancements.

## 📜 License
Licensed under the [MIT License](LICENSE).

---
*Built with ❤️ by the Google Agentic AI Community.*

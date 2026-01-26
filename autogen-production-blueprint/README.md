# AutoGen Production Blueprint 🤖

This is a production-grade template for building multi-agent systems using **Microsoft AutoGen**. It emphasizes modular agent design, secure code execution, and enterprise-level orchestration.

## 🏗 Architecture

The blueprint is organized into specialized layers:

- **`config/`**: Centralized configuration for LLMs and agent parameters.
- **`src/agents/`**: Modular agent definitions with distinct roles and capabilities.
- **`src/workflows/`**: Orchestration logic (Group Chat, Finite State Machines, etc.).
- **`src/tools/`**: Custom Python functions and API integrations.
- **`api/`**: FastAPI implementation for asynchronous agent execution.
- **`observability/`**: Logging, tracing, and cost estimation.

## 🌟 Key Features

- **Sandboxed Execution**: Pre-configured patterns for safe code execution.
- **Modular Conversations**: Easy-to-extend workflow patterns for complex tasks.
- **State Management**: Handling long-running conversations and state persistence.
- **Enterprise Ready**: Built-in health checks and environment-driven configuration.
- **Microservices Architecture**: Serve your agent teams via a robust REST API.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd autogen-production-blueprint
   chmod +x start.sh
   ./start.sh
   ```

2. **Run via CLI**:
   ```bash
   venv/bin/python src/main.py
   ```

3. **Run via API**:
   ```bash
   venv/bin/uvicorn api.main:app --reload
   ```

## ☁️ Deploy to Azure

The blueprint includes production-ready **Infrastructure as Code (Bicep)** for deploying to **Azure Container Apps** (ACA).

### Automated Deployment (CLI)
1. **Login to Azure**: `az login`
2. **Run Deployment**:
   ```bash
   chmod +x scripts/deploy_azure.sh
   ./scripts/deploy_azure.sh
   ```

## 🧹 Cleanup (Absolute Zero Cost)

To ensure no resources remain and stop all charges, run the cleanup script:
```bash
chmod +x scripts/cleanup_azure.sh
./scripts/cleanup_azure.sh
```
This will delete the Resource Group and all associated resources.

```text
autogen-production-blueprint/
├── config/              # LLM and Agent configurations
├── src/                 # Core logic
│   ├── agents/          # Specialized agent definitions
│   ├── workflows/       # Team orchestration logic
│   ├── tools/           # Custom executable tools
│   └── main.py          # CLI entry point
├── api/                 # FastAPI service layer
├── observability/       # Tracing and logging
├── scripts/             # System utilities
└── start.sh             # Developer entry point
```

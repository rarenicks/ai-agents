# OpenAI Agent SDK Production Blueprint 🤖

This is an enterprise-grade template for building multi-agent systems using the **official OpenAI Agent SDK**. It demonstrates the "Handoff" pattern for building modular, specialized agent teams.

## 🏗 Architecture
Organized for production readiness:
- **`src/agents/`**: Official `Agent` definitions and `handoff` logic.
- **`src/workflows/`**: Uses `AgentRunner` for automated handoff orchestration.
- **`api/`**: FastAPI implementation for asynchronous agent execution.
- **`infra/`**: Azure Bicep for scale-to-zero deployment.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd openai-agents-production-blueprint
   # (Standard setup or use start.sh)
   ```

2. **Run via API**:
   ```bash
   venv/bin/uvicorn api.main:app --port 8003
   ```

## ☁️ Deploy to Azure

Includes production-ready **Infrastructure as Code (Bicep)** for **Azure Container Apps**.

```bash
chmod +x scripts/deploy_azure.sh
./scripts/deploy_azure.sh
```

## 🧹 Cleanup
To stop all charges:
```bash
./scripts/cleanup_azure.sh
```

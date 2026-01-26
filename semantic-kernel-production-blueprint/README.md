# Semantic Kernel Production Blueprint 🔮

This is a production-grade template for building multi-agent systems using **Microsoft Semantic Kernel (Python)**. It follows enterprise design patterns, emphasizing modular plugins, kernel isolation, and robust orchestration.

## 🏗 Architecture

The blueprint is organized into specialized layers:

- **`config/`**: Configuration for model providers (Ollama, OpenAI, Azure).
- **`src/agents/`**: Modular agent definitions using the SK Agent Framework.
- **`src/plugins/`**: Native and Semantic plugins (tools) for agents.
- **`src/orchestration/`**: Multi-agent coordination logic (Agent Group Chat).
- **`api/`**: FastAPI implementation for serving agent workflows.
- **`scripts/`**: Utilities for health checks and local model management.

## 🌟 Key Features

- **Hybrid Model Support**: Seamlessly switch between **Ollama**, **Standard OpenAI**, and **Azure OpenAI**.
- **Agent Group Chat**: Production-grade multi-agent orchestration with termination and selection strategies.
- **Enterprise Plugins**: Clean separation of concerns using the Semantic Kernel Plugin architecture.
- **Async First**: Fully asynchronous implementation for high-performance agentic workflows.
- **Observability**: Structured for integration with Azure Monitor or standard logging.

## ☁️ Deploy to Azure

The blueprint includes production-ready **Infrastructure as Code (Bicep)** for deploying to **Azure Container Apps** (ACA). This is the most economical way to run agentic workloads as it scales to zero.

### Option 1: Automated Deployment (CLI)
1. **Login to Azure**: `az login`
2. **Run Deployment**:
   ```bash
   chmod +x scripts/deploy_azure.sh
   ./scripts/deploy_azure.sh
   ```

### Option 2: Manual Portal Deployment
1. Build the Docker image locally: `docker build --platform linux/amd64 -t semantic-kernel-blueprint .`
2. Create an **Azure Container Registry** (ACR) and push the image.
3. Create an **Azure Container App** pointing to that image.
4. Add your `OPENAI_API_KEY` or `AZURE_OPENAI_API_KEY` to the **Secrets** section of the Container App.

## 🧹 Cleanup (Absolute Zero Cost)

To ensure no resources remain and stop all charges, run the cleanup script:
```bash
chmod +x scripts/cleanup_azure.sh
./scripts/cleanup_azure.sh
```
This will delete the Resource Group and all associated resources.

## 🛠 Project Structure

```text
semantic-kernel-production-blueprint/
├── config/              # Kernel and Model settings
├── src/                 # Core logic
│   ├── agents/          # Specialized agent implementations
│   ├── plugins/         # Native and Semantic plugins
│   ├── orchestration/   # Group Chat and Workflow logic
│   └── main.py          # CLI entry point
├── api/                 # FastAPI service layer
├── scripts/             # System utilities
└── start.sh             # Setup and developer entry point
```

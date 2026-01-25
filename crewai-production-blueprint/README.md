# CrewAI Production Blueprint 🚀

This is a production-grade template for building multi-agent systems using **CrewAI**. It follows enterprise standards for configuration, modularity, observability, and deployment.

## 🏗 Architecture

The blueprint is organized into specialized layers:

- **`config/`**: YAML-defined Agents and Tasks. Separates logic from prompts.
- **`src/`**: Core agent logic and custom enterprise tools.
- **`api/`**: FastAPI integration for serving your Crew as a microservice.
- **`observability/`**: Integration with tracing tools (Agents monitoring).
- **`evaluation/`**: Performance metrics and quality guardrails.
- **`scripts/`**: Automation scripts for health checks and deployment.

## 🌟 Key Features

- **YAML-First Config**: Modify agent behavior without touching Python code.
- **Microservices Ready**: Built-in FastAPI wrapper for external integration.
- **Production Observability**: Configured for deep tracing of agent thought processes.
- **Enterprise Tools**: Pre-configured patterns for safe tool integration.
- **Standardized Logging**: Unified logging format for production monitoring.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd crewai-production-blueprint
   chmod +x start.sh
   ./start.sh
   ```

2. **Configure Agents**:
   Edit `config/agents.yaml` and `config/tasks.yaml` to define your specific use case.

3. **Run via CLI**:
   ```bash
   uv run python src/main.py
   ```

4. **Run via API**:
   ```bash
   uv run fastapi dev api/main.py
   ```

## 🛠 Project Structure

```text
crewai-production-blueprint/
├── config/              # Agent and Task YAML files
├── src/                 # Main Python logic
│   ├── tools/           # Custom enterprise tools
│   ├── crew.py          # Crew definition
│   └── main.py          # CLI entry point
├── api/                 # FastAPI service
├── observability/       # Tracing and monitoring
├── scripts/             # System utilities
└── start.sh             # Main entry point for developers
```

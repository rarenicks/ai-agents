# Google AI Agent System - Enterprise Edition

This project is a reference implementation of an **Enterprise Multi-Agent System** specialized for the Google ecosystem. It functions as a platform for building, deploying, and monitoring fleets of autonomous agents.

## 🌟 Enterprise Architecture

The system implements the **Supervisor Pattern** for multi-agent orchestration.

```mermaid
graph TD
    User --> Engine[Agent Engine (FastAPI)]
    Engine --> Registry[Agentspace Registry]
    Registry --> Team[Team Alpha (Supervisor)]
    
    subgraph "Team Alpha"
    Team -->|Delegates| Researcher[Researcher Agent]
    Team -->|Delegates| Writer[Writer Agent]
    Researcher -->|Search Tools| Web
    Writer -->|Formatting| DocGen
    end

    Engine --> Observability[Observability Layer]
    Observability --> Logs[Google Cloud Logging (Simulated)]
```

## 🚀 Key Features

### 1. Agentspace Registry (Powered by Google ADK)
- **ADK Integration**: Leverages the `google-adk` package for enterprise-grade agent orchestration and delegation.
- **Dynamic Loading**: Agents are registered in `engine/space/registry.py` and lazily instantiated.
- **Teams**: Support for single agents and hierarchical teams using the ADK `Coordinator` pattern.

### 2. Hierarchical Teams (The "Brain")
- **Supervisor (LlmAgent)**: An ADK-based orchestrator that routes tasks between workers using native delegation.
- **Workers**:
    - **Researcher**: Equipped with search tools to gather facts.
    - **Writer**: Specialized in synthesizing information into Markdown reports.

### 3. Local & Cloud Versatility
- **Model Agnostic**: Supports Google Gemini via Vertex AI/AI Studio or local LLMs (like Llama 3) via **Ollama** and **LiteLLM**.
- **Enterprise Ready**: Designed to scale from local development to production on Google Cloud Agent Engine.

### 4. Deep Observability
- **Trace Logging**: Every thought, tool call, and state transition is captured.
- **Auditable**: Designed to connect with Google Cloud Trace in production.

## 🛠 System Components

- **`engine/agents/supervisor.py`**: The team orchestrator logic.
- **`engine/agents/researcher.py`**: Validates data sources.
- **`engine/agents/writer.py`**: Generates final output.
- **`frameworks/a2a/`**: Inter-agent protocols.
- **`frameworks/mcp/`**: External tool integration.

## ⚡️ Quick Start

1. **Setup**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   ```

2. **Launch Engine**:
   ```bash
   ./start.sh
   # API is now live at http://localhost:8000
   ```

3. **Web Interface**:
   ```bash
   ./venv/bin/streamlit run client/web_client.py
   ```

## 🧪 Evaluation

Run the automated test suite to validate the full team's performance:
```bash
./venv/bin/python3 evaluation/run_eval.py
```

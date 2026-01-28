# LlamaIndex Production Blueprint 🦙

This blueprint demonstrates a production-grade implementation of **LlamaIndex**, focusing on data-centric agents and RAG (Retrieval-Augmented Generation).

## 🏗 Architecture
- **`src/agents/`**: ReAct agents with integrated query engine tools.
- **`data/`**: Source documents for the knowledge base.
- **`api/`**: FastAPI implementation for serving agent queries.
- **`config/`**: Managed environment settings.

## 🌟 Key Features
- **ReAct Agent Design**: Agents that can reason and act upon your proprietary data.
- **RAG Integration**: Built-in retrieval engine that grounds responses in provided documents.
- **Strict Data Control**: Demonstrates how to point agents at specific local or cloud document directories.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd llamaindex-production-blueprint
   chmod +x start.sh
   ./start.sh
   ```

2. **Run API**:
   ```bash
   venv/bin/uvicorn api.main:app --port 8006 --reload
   ```

3. **Interact**:
   ```bash
   curl -X POST http://localhost:8006/chat \
        -H "Content-Type: application/json" \
        -d '{"query": "How many days can I work from home according to company policy?"}'
   ```

## 🔍 Data Sources
To add more knowledge, simply drop markdown, PDF, or text files into the `data/` folder and restart the API.

# LlamaIndex Production Blueprint

> **The Data-Centric Agent Framework (RAG)**

This blueprint demonstrates a production-ready **RAG (Retrieval-Augmented Generation)** agent using **LlamaIndex**. While other frameworks focus on orchestration, LlamaIndex focuses on **connecting data to LLMs**.

---

## 📚 Educational Guide: Understanding LlamaIndex

### 🧠 Core Philosophy
Generic LLMs don't know your private data. LlamaIndex solves this by:
1.  **Indexing**: Converting your documents into searchable vectors.
2.  **Querying**: Finding relevant chunks.
3.  **Synthesis**: Combining those chunks with a prompt to answer questions.
In this blueprint, we go a step further and wrap this RAG pipeline into an **Agent** that can "reason" over the data.

### 🔑 Key Concepts in this Blueprint
1.  **Vector Store Index**: In `src/agents/policy_agent.py`, we ingest `data/policy.md`. LlamaIndex chunks this text and creates a searchable index.
2.  **Query Engine as a Tool**: We don't just "chat" with the data. We wrap the `QueryEngine` as a functional **Tool** (`company_policy`). This allows the agent to decide *when* to look up policy (e.g., "What is the refund limit?") vs. *when* to just use general knowledge (e.g., "Write a polite email").
3.  **ReAct Pattern**: We use the `ReActAgent` (Reason + Act). The agent "thinks" about the user's question, "acts" by calling the query tool, observes the policy snippet, and then synthesizes a final answer.

### 🏗 Architecture Explained
```
llamaindex-production-blueprint/
├── src/
│   └── agents/
│       └── policy_agent.py    # <--- THE RAG AGENT. index creation + tool wrapping + agent init.
├── data/
│   └── policy.md              # <--- THE KNOWLEDGE. A sample markdown file acting as the knowledge base.
├── api/
│   └── main.py                # <--- THE API. Exposes the RAG agent via FastAPI.
├── config/
│   └── settings.py            # <--- CONFIG. Manages chunk sizes and API keys.
└── test_llamaindex.py         # <--- RAG TEST. Verifies the agent can actually find the data.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
Initialize the environment:
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`.*

### 2. 🧪 Test RAG Retrieval
Run the test script to ask a question about the dummy policy file:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_llamaindex.py
```
*You should see the agent look up the "Remote Work Policy" effectively.*

### 3. 🌐 Run the API Server
Deploy the RAG service:
```bash
python api/main.py
```

### 4. 📝 Modify the Data
Edit `data/policy.md`. Change the "Meal Allowance" to `$100`. Restart the server and ask the agent about the allowance. **It will instantly know the new value without retraining!**

---

## 🛡 Production Readiness Checklist

| Feature | Implemented? | Production Recommendation |
| :--- | :---: | :--- |
| **Ingestion** | ✅ (Simple) | Use `LlamaParse` for complex PDFs/Docs instead of simple text readers. |
| **Vector DB** | ⚠️ (Local) | Currently memory-based. Switch to Qdrant/Pinecone for handling large datasets. |
| **Chunking** | ✅ | Configured in `config/settings.py`. Tuning `CHUNK_SIZE` is critical for performance. |
| **Reasoning** | ✅ | `ReActAgent` is used. For very complex tasks, consider `FunctionCallingAgent` (if using OpenAI). |

## 💡 Pro Tip
LlamaIndex creates a storage folder locally (`storage/`) if you persist it. In production, you never want to re-index data on every startup. You should build the index *once* (in a build pipeline), save it to disk/S3, and have your API simply *load* it for faster startup times.

# ai-agents (Codebank)

Welcome to the **ai-agents** codebank. This repository is a collection of various AI agent implementations, ranging from educational tutorials to enterprise-grade systems.

## 🚀 Featured Projects

### 1. Google AI Agent System (ADK)
**Directory: `google-ai-agent-system/`**
An enterprise-grade multi-agent system built using the **Google Agent Development Kit (ADK)**. 
- **Supervisor Pattern**: Uses a central Supervisor to delegate tasks between specialized Researcher and Writer agents.
- **Local & Cloud Support**: Integrated with Google Gemini and local models (LLama 3) via Ollama.
- **Observability**: Built-in trace logging and performance monitoring.

### 2. Agents From Scratch (LangGraph Workshop)
**Directory: `notebooks/`, `src/email_assistant/`**
A guide to building agents from scratch, culminating in an "ambient" agent that manages email via the Gmail API.
- **4 Sections**: Basics, Evaluation, Human-in-the-loop, and Memory.
- **Framework**: Built primarily using LangGraph.

### 3. Crew AI Implementations
- **[Basic Crew AI Tutorial](basic-crew-ai-agent-tutorial)**: Implementation and setup instructions for Content Writer Agents using Crew AI.

### 4. LangChain Agent Tutorials
- **[Basic LangChain Tutorial](basic-langchain-agent-tutorial)**: Chaining together language models and tools for complex reasoning.

---

## 🛠 Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rarenicks/ai-agents.git
    cd ai-agents
    ```

2. **Explore a Project**:
    Each subdirectory contains its own `README.md` with specific setup instructions. For the enterprise system:
    ```bash
    cd google-ai-agent-system
    ./start.sh
    ```

3. **Environment Setup**:
    Most projects require a `.env` file. See `.env.example` in the respective directories.

---

## 📈 Future Plans
- [ ] Integration with more MCP (Model Context Protocol) tools.
- [ ] Advanced RAG (Retrieval Augmented Generation) agent templates.
- [ ] Autonomous coding assistants specialized for various languages.

## 🤝 Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📜 License
This project is licensed under the MIT License.

---
*For support or inquiries, contact [ai.avdhesh@gmail.com](mailto:ai.avdhesh@gmail.com).*

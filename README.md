# AI Agent Blueprints

A collection of functional reference implementations for major AI agent frameworks.

## 🎯 Purpose

The landscape of AI agent frameworks is fragmented and rapidly evolving. This repository serves as a **learning laboratory** to help engineers understand, compare, and experiment with different approaches to building agentic systems.

This is **not** a production-ready framework or a deployment solution. It is a set of "blueprints"—code scaffolds designed to accelerate your understanding of how each specific framework handles modularity, state, tooling, and orchestration.

## 👤 Target Audience

**This repository is for:**
-   **Engineers** evaluating which framework fits their specific use case.
-   **Learners** wanting to see functional code rather than abstract documentation.
-   **Prototypers** needing a quick working environment to test an idea.

**This repository is NOT for:**
-   **Production Deployment**: These examples lack the necessary security, observability, and error handling for critical systems.
-   **Scalability Testing**: The implementations are optimized for educational clarity, not high-throughput concurrency.

## 📂 Frameworks Overview

Each directory contains a standalone implementation using a specific framework, demonstrating its core philosophy.

| Framework | Core Philosophy | Best For Learning... |
| :--- | :--- | :--- |
| **[Google ADK](./google-ai-agent-system)** | Systemic Design | How to structure large, multi-agent systems with clear delegation. |
| **[LangGraph](./langgraph-blueprint)** | Graph Theory | Managing complex, cyclic state and time-travel debugging. |
| **[CrewAI](./crewai-blueprint)** | Role-Playing | Orchestrating teams with distinct personas and hierarchical tasks. |
| **[PydanticAI](./pydantic-ai-blueprint)** | Type Safety | Using Python type systems to enforce LLM output structure. |
| **[Agno (Phidata)](./agno-blueprint)** | Storage-First | Persisting long-running agent sessions in a database. |
| **[LlamaIndex](./llamaindex-blueprint)** | Data-Centric | Integrating agents deeply with vector search and RAG pipelines. |
| **[OpenAI Swarm](./openai-agents-blueprint)** | Minimalist | Understanding native handoffs without heavy abstraction layers. |
| **[AutoGen](./autogen-blueprint)** | Conversational | Sandboxed code execution and multi-agent chat loops. |
| **[Semantic Kernel](./semantic-kernel-blueprint)** | Plugin-Based | Integrating LLMs into existing enterprise applications (C#/.NET roots). |
| **[DSPy](./dspy-blueprint)** | Declarative | "Programming" prompts through optimization rather than manual engineering. |

## 🛠 Usage Guide

Each blueprint is self-contained with its own dependencies and configuration (no shared root dependencies).

1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/rarenicks/ai-agents.git
    cd ai-agents
    ```

2.  **Select a Framework**:
    Decide what you want to learn (e.g., "How does LangGraph handle loops?").
    ```bash
    cd langgraph-blueprint
    ```

3.  **Initialize**:
    We provide a standard setup script for detailed environment setup.
    ```bash
    chmod +x start.sh
    ./start.sh
    ```
    *Add your API keys to the generated `.env` file.*

4.  **Experiment**:
    Read the `README.md` in that specific folder for a specific "Deep Dive" explanation, then run the provided API or CLI scripts.

## ⚠️ Disclaimer & Limitations

-   **Security**: These examples expose endpoints that are not secured. Do not expose them to the public internet.
-   **Costs**: Running these agents involves calls to paid LLM APIs (OpenAI, Gemini, etc.). Monitor your usage carefully.
-   **Stability**: AI frameworks change frequently. These blueprints are snapshots in time and may require updates to match the latest library versions.

## 🤝 Contributions

We welcome contributions that fix bugs, update dependencies, or clarify the educational content. Please ensure new PRs focus on readability and conceptual clarity over feature bloat.

## 📜 License

MIT License.

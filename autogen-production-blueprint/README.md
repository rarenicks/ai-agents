# AutoGen Production Blueprint

> **The Conversational Multi-Agent Framework**

This blueprint demonstrates the power of Microsoft's **AutoGen**, a framework where agents are **Conversable**. Agents interact with each other (and users) essentially by sending messages involved in a group chat, capable of autonomous loop execution.

---

## 📚 Educational Guide: Understanding AutoGen

### 🧠 Core Philosophy
AutoGen abstracts everything as a "Conversation".
- **UserProxyAgent**: An agent that acts as a proxy for the human (used to execute code or ask for input).
- **AssistantAgent**: An AI agent that can reason and write code.
- **GroupChat**: A chat room where multiple agents (Coders, Reviewers, Products Managers) talk until a termination condition is met.

### 🔑 Key Concepts in this Blueprint
1.  **Two-Agent Conversation**: In `src/agents/group_chat.py`, we set up a classic pair: An `AssistantAgent` (The Solver) and a `UserProxyAgent` (The Executor). The Assistant writes code, and the UserProxy *actually executes it* locally (in a Docker container for safety) and reports the result back.
2.  **Docker Execution**: This blueprint strictly enforces **Docker-based code execution**. Allowing agents to run raw Python on your host machine is a security nightmare. We use AutoGen's `DockerCommandLineCodeExecutor` to prevent this.
3.  **Termination Conditions**: How does the agent stop? We define an `is_termination_msg` function. If the agent says "TERMINATE", the loop ends.

### 🏗 Architecture Explained
```
autogen-production-blueprint/
├── src/
│   └── agents/
│       └── group_chat.py      # <--- THE CHAT. Defines the Assistant and UserProxy interaction.
├── api/
│   └── main.py                # <--- THE API. A REST interface to trigger the conversation.
├── Dockerfile                 # <--- THE SANDBOX. Defines the environment where agent code runs.
├── work_dir/                  # <--- THE WORKSPACE. A shared folder mounted to the Docker container.
└── test_autogen.py            # <--- THE TEST. Runs the conversation locally.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`.*

### 2. 🐳 Prerequisite: Docker
**Crucial Step**: You must have Docker Desktop running. AutoGen needs to spin up a container to execute the code the AI writes.

### 3. 🧪 Run the Two-Agent Loop
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_autogen.py
```
*Watch the magic: The Assistant will write a python script to `work_dir/`, the UserProxy will run it in Docker, and the result will be printed.*

### 4. 🌐 Run the API Server
```bash
python api/main.py
```

---

## 🛡 Production Readiness Checklist

| Feature | Implemented? | Production Recommendation |
| :--- | :---: | :--- |
| **Sandboxing** | ✅ | Docker execution is mandatory in this blueprint. **Never disable this in production.** |
| **Human-in-the-loop** | Limited | AutoGen supports `human_input_mode="ALWAYS"`. In an API context, this is tricky; often better to set to `NEVER` for autonomous tasks. |
| **State Management** | ❌ | AutoGen chats are usually ephemeral. For long-term memory, integration with vector DBs (like Chroma) is required. |
| **Costs** | ⚠️ | Code-writing loops can be long. Monitor step counts and token usage aggressively. |

## 💡 Pro Tip
AutoGen shines at **Code Generation**. Try asking the agent to "Plot a chart of the stock price of NVDA for the last month". It will write a Python script using `yfinance` and `matplotlib`, install the libs in Docker, run it, and save the `.png` file to your `work_dir/`. A complete data analyst in a box!

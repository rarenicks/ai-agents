# Semantic Kernel Blueprint

> **The Enterprise Integration Framework**

This blueprint showcases Microsoft's **Semantic Kernel (SK)**. Unlike other frameworks that try to "be the agent," Semantic Kernel is designed to integrate LLMs into **existing enterprise codebases**. It treats prompts as "Semantic Functions" alongside native code ("Native Functions").

---

## 📚 Educational Guide: Understanding Semantic Kernel

### 🧠 Core Philosophy
SK envisions a world where your app interacts with "Plugins".
- **Plugins**: Bundles of capabilities (e.g., a "MathPlugin", an "EmailPlugin").
- **Kernel**: The central processor that routes requests to the right plugin.
- **Planners**: The "Agent" part. A Planner takes a user goal (e.g., "Email the sum of 5+5 to Bob") and automatically chains the MathPlugin and EmailPlugin together.

### 🔑 Key Concepts in this Blueprint
1.  **The Kernel**: In `src/kernel_setup.py`, we initialize the Kernel and attach the OpenAI Service. This `kernel` object is passed around your app.
2.  **Plugins as Classes**: Look at `src/plugins/MathPlugin.py`. It's a standard Python class decorated with `@kernel_function`. This allows the LLM to "see" your python methods as tools.
3.  **Basic Planner**: We use the `FunctionCallingStepwisePlanner`. This is the "brain" that looks at all available plugins and decides the sequence of actions to take.

### 🏗 Architecture Explained
```
semantic-kernel-blueprint/
├── src/
│   ├── plugins/
│   │   └── MathPlugin.py      # <--- NATIVE FUNCTION. A python class exposed to AI.
│   └── kernel_setup.py        # <--- THE KERNEL. Configures the SDK and Service.
├── api/
│   └── main.py                # <--- THE API. FastAPI endpoint using the Planner.
├── config/
│   └── settings.py            # <--- CONFIG. Maps environment variables.
└── test_sk.py                 # <--- THE TEST. Runs a simple plan locally.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`.*

### 2. 🧪 Test the Planner
Run the test script to see the planner use the `MathPlugin`:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_sk.py
```
*Query: "What is the square root of 144?" -> Planner calls MathPlugin.sqrt(144).*

### 3. 🌐 Run the API Server
```bash
python api/main.py
```
```bash
curl -X POST http://localhost:8000/process \
     -H "Content-Type: application/json" \
     -d '{"request": "Calculate 50 divided by 2."}'
```

---

## 🛡 Blueprint Features Checklist

| Feature | Implemented? | Notes |
| :--- | :---: | :--- |
| **Enterprise Auth** | ✅ | SK supports Azure AD auth natively (especially with Azure OpenAI). |
| **Filters** | ❌ | Implement `AutoFunctionInvocationFilter` to intercept and approve tool calls before they execute. |
| **Memory** | ❌ | This blueprint is stateless. SK supports "Semantic Memory" (vector DBs) which should be added for RAG. |
| **Telemetry** | ✅ | SK has deep integration with Azure Monitor and OpenTelemetry. |

## 💡 Pro Tip
Semantic Kernel is unique because it supports **Prompt Templating in text files**. You can create a folder structure with `skprompt.txt` and `config.json` to define "Semantic Functions" (pure prompts) that look and feel just like your Python functions. This allows non-coders to "write code" for the application!

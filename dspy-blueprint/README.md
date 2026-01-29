# DSPy Blueprint

> **The Framework for Programming—Not Prompting—LMs**

This blueprint demonstrates **DSPy** (Declarative Self-improving Python). DSPy completely rethinks how we interact with LLMs. Instead of manually tuning string prompts ("Please be nice", "Think step by step"), you define **Signatures** (I/O specs) and **Modules** (logic layers), and let DSPy's optimizers tune the prompts for you.

---

## 📚 Educational Guide: Understanding DSPy

### 🧠 Core Philosophy
Machine Learning moved from manual feature engineering to deep learning layers. DSPy moves NLP from manual "prompt engineering" to **declarative modules**.
- **Signature**: Defines *what* you want (Input -> Output fields). It is prompt-agnostic.
- **Module**: Defines *how* to solve it (e.g., Chain of Thought, ReAct, RAG).
- **Teleprompter (Optimizer)**: The "Compiler". It takes your module + some training examples and *automagically* writes the best possible prompt for your specific LLM.

### 🔑 Key Concepts in this Blueprint
1.  **Declarative Signatures**: In `src/modules/fact_checker.py`, we define `FactChecker` with fields `context`, `claim` -> `reasoning`, `assessment`. We never write "You are a helpful assistant..."
2.  **ChainOfThought**: We wrap our signature in `dspy.ChainOfThought`. This automatically injects the logic to "Thinking step-by-step" without us writing instructions.
3.  **Forward Pass**: The usage looks like PyTorch: `module.forward(input)`. This makes integration into software engineering pipelines trivial.

### 🏗 Architecture Explained
```
dspy-blueprint/
├── src/
│   └── modules/
│       └── fact_checker.py    # <--- THE MODULE. Defines the dspy.Signature and dspy.Module.
├── api/
│   └── main.py                # <--- THE API. Exposes the compiled module via FastAPI.
├── config/
│   └── settings.py            # <--- CONFIG. Standard Pydantic settings.
└── test_dspy.py               # <--- THE TEST. Runs the module locally.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`.*

### 2. 🧪 Run the Module
Test the fact-checking logic:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_dspy.py
```
*Observe how DSPy automatically generates the "Reasoning" field because we used ChainOfThought.*

### 3. 🌐 Run the API Server
```bash
python api/main.py
```
```bash
curl -X POST http://localhost:8000/check \
     -H "Content-Type: application/json" \
     -d '{"context": "Paris is the capital of France.", "claim": "Paris is in Germany."}'
```

---

## 🛡 Blueprint Features Checklist

| Feature | Implemented? | Notes |
| :--- | :---: | :--- |
| **Optimization** | ❌ (Basic) | Crucial step missing: Use `BootstrapFewShot` to "compile" this module with labeled examples (`trainset`) to maximize accuracy. |
| **Caching** | ❌ | DSPy has a built-in cache. Enable it for development speed. |
| **Assertions** | ❌ | Use `dspy.Assert` to enforce constraints (e.g., "Reasoning must be < 50 words") during runtime. |
| **Containerization**| ✅ | `Dockerfile` included. |

## 💡 Pro Tip
The prompt you see running is "Zero Shot". To make it strictly better, create a list of 5 examples (`dspy.Example`), and pass them to an Optimizer (`dspy.teleprompt.BootstrapFewShot`). The optimizer will verify which examples actually help the model and modify the prompt dynamically!

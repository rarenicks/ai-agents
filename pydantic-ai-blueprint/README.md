# PydanticAI Production Blueprint

> **The Type-Safe Agent Framework**

This blueprint showcases **PydanticAI**, a framework built by the creators of Pydantic. It focuses on **Type Safety**, **Structured Outputs**, and **Developer Experience**. If you love Python type hints and hate "stringly typed" programming, this is your framework.

---

## 📚 Educational Guide: Understanding PydanticAI

### 🧠 Core Philosophy
Many agent frameworks rely on loose dictionaries or chaotic prompt engineering to structure data. PydanticAI enforces rigor:
- **Agents are Functions**: They accept typed inputs and return typed outputs.
- **Dependency Injection**: It has a robust system (`RunContext`) to inject DB connections or API keys into tools safely.
- **Validation**: If an LLM hallucinates a bad structure, PydanticAI catches it *before* it crashes your app.

### 🔑 Key Concepts in this Blueprint
1.  **Strict Typed Agents**: In `src/agents/support_agent.py`, notice how the `SupportResult` model defines exactly what the agent *must* return (a `support_advice` string and a `risk_level` integer).
2.  **Dependency Injection (`Deps`)**: We don't hardcode user names or database mocks. We define a `SupportDeps` dataclass and pass it into the agent at runtime. This makes testing trivial—just pass a mock `Deps` object!
3.  **Logfire Integration**: This blueprint comes pre-wired with Logfire, Pydantic's observability platform. It auto-magically traces validation errors and LLM calls.

### 🏗 Architecture Explained
```
pydantic-ai-blueprint/
├── src/
│   ├── agents/
│   │   └── support_agent.py   # <--- THE LOGIC. Defines the Agent, Deps, and Result Models.
│   └── models/
│       └── support.py         # <--- THE TYPES. Pydantic models for inputs/outputs.
├── api/
│   └── main.py                # <--- THE API. FastAPI router that injects deps into the agent.
├── ping_logfire.py            # <--- OBSERVABILITY. A quick script to test your Logfire connection.
└── test_pydantic_ai.py        # <--- TESTING. Unit tests ensuring the agent respects types.
```

---

## 🚀 Getting Started

### 1. 🛠 Setup
```bash
chmod +x start.sh
./start.sh
```
*Action required: Update `.env` with `OPENAI_API_KEY`. Optional: Add `LOGFIRE_TOKEN`.*

### 2. 🧪 Test Type Safety
Run the test script. Notice how it asserts the response structure:
```bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python test_pydantic_ai.py
```

### 3. 🌐 Run the API Server
Deploy the type-safe agent:
```bash
python api/main.py
```
Send a request:
```bash
curl -X POST http://localhost:8000/support \
     -H "Content-Type: application/json" \
     -d '{"ticket_content": "My computer won not turn on", "user_name": "Alice"}'
```
*Note the response matches the `SupportResult` schema exactly!*

---

## 🛡 Production Readiness Checklist

| Feature | Implemented? | Production Recommendation |
| :--- | :---: | :--- |
| **Structured Output** | ✅ | Guaranteed by Pydantic models. |
| **Dependency Injection** | ✅ | Fully used for passing user context. |
| **Observability** | ✅ | Logfire is configured (requires token). |
| **Testing** | ✅ | `test_pydantic_ai.py` demonstrates how to test agents deterministically. |
| **Containerization**| ✅ | `Dockerfile` included. |

## 💡 Pro Tip
Go to `src/models/support.py` and add a validator (e.g., `@field_validator`) to `risk_level` ensuring it's between 1-10. If the LLM tries to return "11", Pydantic will catch it, reject it, and force the LLM to retry automatically!

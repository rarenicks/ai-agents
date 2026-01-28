# PydanticAI Production Blueprint 🛡️

This blueprint demonstrates a production-grade implementation of **PydanticAI**, the agentic framework from the creators of Pydantic. It focuses on type safety, structured outputs, and seamless observability via **Logfire**.

## 🏗 Architecture
- **`src/models/`**: Pydantic models for strictly typed agent responses.
- **`src/agents/`**: Dependency-injected agents with tool integration.
- **`api/`**: FastAPI implementation with Logfire instrumentation.
- **`config/`**: Environment-driven settings.

## 🌟 Key Features
- **Strictly Typed Responses**: Agents return Pydantic models, not just strings.
- **Dependency Injection**: Pass state (customer data, DB connections) safely into tools.
- **Logfire Integration**: Built-in observability for tracing model calls and tool execution.

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   cd pydantic-ai-production-blueprint
   chmod +x start.sh
   ./start.sh
   ```

2. **Run Tests**:
   ```bash
   venv/bin/python test_pydantic_ai.py
   ```

3. **Run API**:
   ```bash
   venv/bin/uvicorn api.main:app --port 8004 --reload
   ```

## 🔍 Observability
Enable **Logfire** by adding your token to `.env`:
```env
LOGFIRE_TOKEN=your_token_here
```
Get a free token at [logfire.pydantic.dev](https://logfire.pydantic.dev).

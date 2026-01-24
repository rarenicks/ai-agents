# Health & Operations

Monitoring the health of a multi-agent system is critical for maintaining reliable enterprise service. This project provides multiple layers of diagnostic tools.

## 🏥 Health Endpoints

The API includes two primary health-related endpoints:

### 1. `/health`
Returns the immediate status of the FastAPI server, a list of active agents in the registry, and a session service heartbeat.
- **Use Case**: Load balancer health checks.

### 2. `/agent/health/check`
Triggers a deeper diagnostic run. It iterates through all registered agents and calls their assigned health check functions.
- **Use Case**: Infrastructure alerts and proactive observability.

---

## 🧪 System Health Script

**File**: `scripts/system_health.py`

A comprehensive command-line tool for developers to verify the ecosystem end-to-end.

### What it checks:
- **Connectivity**: Can it reach the FastAPI Engine?
- **Registry Integrity**: Are the core agents (Team Alpha) registered and healthy?
- **Agent Roundtrip**: Can the LLM reason and respond to a basic "Hello" message?
- **Tool Integration**: Can the agents successfully reach the MCP client and simulate a tool call?

### Running the Check:
```bash
./venv/bin/python3 scripts/system_health.py
```

---

## 📝 Performance Optimization

### 💨 Context Caching
To reduce token usage and latency in long-running sessions, the system is configured with `ContextCacheConfig`. 
- **TTL**: 3600 seconds (1 hour).
- **Behavior**: LLM inputs for the same session are cached at the provider level where supported (e.g., Google Gemini).

### ⏯ Resumability
Sessions are built with `is_resumable: True`. This allows the `Runner` to save state after tool calls. If a session times out or an error occurs, the next request with the same `session_id` can resume from the exact point of interruption.

# Enterprise Plugins - Safety & Observability

The Google AI Agent System utilizes the **ADK Plugin System** to provide cross-cutting concerns that apply to all agents in the ecosystem. This ensures a consistent security and monitoring layer without cluttering individual agent logic.

## 📊 Enterprise Observability Plugin

**File**: `observability/monitor.py`

The `EnterpriseObservabilityPlugin` intercepts every critical point in the agent lifecycle. It is essential for auditing, debugging, and performance optimization.

### Key Monitored Events:
- **`before_agent_callback`**: Logs the start of an agent's turn and the current Session ID.
- **`before_tool_callback`**: Logs which tool is about to run and with what arguments.
- **`after_tool_callback`**: Captures and truncates tool results for history logs.
- **`after_model_callback`**: Extracts LLM usage metadata (tokens, latency) from the response.
- **`on_tool_error_callback`**: Logs failures and exception details for proactive maintenance.

### Example Log Output:
```text
2026-01-24 03:26:31 - EnterpriseMonitor - INFO - [Agent:Senior_Researcher] Invocation started.
2026-01-24 03:26:31 - EnterpriseMonitor - INFO - [Tool:web_search] Starting execution with args: {'query': 'Google Gemini news'}
2026-01-24 03:26:31 - EnterpriseMonitor - INFO - [LLM] Model responded. Usage: total_token_count=1344
```

---

## 🛡 Agent Policy Plugin

**File**: `engine/policy.py`

The `AgentPolicyPlugin` enforces corporate guardrails and security protocols across the entire agent fleet.

### 🔐 Security Intercepts
The plugin monitors tool execution and can block sensitive actions.
- **Sensitive Tools**: Specific tools (like `mcp_read_document`) can be marked as sensitive.
- **Access Control**: It implements logic to verify `access_level` flags (e.g., blocking `write` operations unless an `authorized` flag is present).

### 📝 Dynamic System Instruction (DSI)
Before every model call, the plugin injects a **Global Policy Block** into the system prompt. This ensures the model always follows safety guidelines even if not explicitly mentioned in the agent's specific instructions.

**Injected Policy Example:**
> `[ENTERPRISE POLICY]: Always protect PII. Never disclose internal document IDs to external search results.`

---

## 🛠 Integration
To add new plugins, update the `App` initialization in `engine/main.py`:

```python
adk_app = App(
    name="Agent_Fleet",
    root_agent=supervisor,
    plugins=[
        EnterpriseObservabilityPlugin(),
        AgentPolicyPlugin(sensitive_tools=["mcp_read_document"]),
        # Add custom plugins here
    ]
)
```

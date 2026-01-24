# Tools & Model Context Protocol (MCP)

This project features a hybrid tool ecosystem: local framework-agnostic Python tools and remote enterprise tools exposed via **MCP**.

## 🛠 Local Tools (Core)

Local tools are simple Python functions stored in the `tools/` directory. By keeping them framework-agnostic (no decorators like `@tool`), they remain reusable across different agent frameworks or simple scripts.

| Tool Name | File | Description |
| :--- | :--- | :--- |
| `web_search` | `search_tool.py` | Live web data retrieval via DuckDuckGo. |
| `calculate_length` | `basic_tools.py` | Utility for string analysis. |
| `get_weather` | `basic_tools.py` | Real-time weather data simulation. |

---

## 🌐 Model Context Protocol (MCP) Integration

**File**: `frameworks/mcp/client.py`

The system implements a robust client for tool discovery. MCP allows agents to connect to remote "Tool Servers" that host specialized enterprise capabilities.

### 🔄 Discovery & Wrapping
The `get_mcp_tools()` factory function performs the following steps:
1. **Connects** to the MCP server endpoint.
2. **Discovers** available tools and their JSON Schema declarations.
3. **Wraps** each remote tool into a native ADK `BaseTool` (specifically `MCPTool`).
4. **Exposes** the explicit parameter schema to the LLM to prevent argument hallucination.

### 📦 Discovered MCP Tools (Simulation)
Currently, the system simulates discovery of the following enterprise tools:
- `mcp_read_document`: Secure internal knowledge base access.
- `mcp_get_system_metrics`: Real-time infrastructure monitoring.

---

## 🏗 Adding New Tools

### 1. Adding a Local Tool
1. Create a function in `tools/`.
2. Add it to an agent's `tools` list in their builder function (e.g., `engine/agents/researcher.py`).

### 2. Adding an MCP Tool
MCP tools are managed by the remote server. The agent system will automatically discover them on startup as long as the server URL is configured in `get_mcp_tools()`.

```python
# From researcher.py
mcp_tools = get_mcp_tools("http://your-mcp-server:8080")
researcher = Agent(..., tools=[web_search] + mcp_tools)
```

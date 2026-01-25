from typing import List, Callable, Dict, Any, Optional
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types

class MCPClient:
    """
    Simulated Model Context Protocol (MCP) Client.
    Discovers tools from a remote server and exposes them to the ADK ecosystem.
    """
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.connected = False

    def connect(self):
        """Simulate connecting to an MCP server."""
        print(f"[MCP] Connecting to server at {self.server_url}...")
        self.connected = True
        print("[MCP] Connected via protocol v1.0")

    def list_tools(self) -> List[Dict[str, Any]]:
        """Fetch available tools from the MCP server."""
        if not self.connected:
            raise ConnectionError("MCP Client not connected")
        
        # Mock responses mimicking real MCP tool discovery
        return [
            {
                "name": "mcp_read_document",
                "description": "Enterprise secure document reader (MCP). Accesses internal knowledge base.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "document_id": {"type": "string", "description": "The unique ID of the document."},
                        "access_level": {"type": "string", "enum": ["read", "read_write"], "default": "read"}
                    },
                    "required": ["document_id"]
                }
            },
            {
                "name": "mcp_get_system_metrics",
                "description": "Retrieve real-time system performance metrics (MCP).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metric_type": {"type": "string", "enum": ["cpu", "memory", "latency"]}
                    }
                }
            }
        ]

    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool on the MCP server."""
        print(f"[MCP] Calling remote tool {tool_name} with {arguments}")
        
        if tool_name == "mcp_read_document":
            doc_id = arguments.get("document_id", "unknown")
            return {"content": f"Secure content for document {doc_id}. Classification: Internal."}
        
        if tool_name == "mcp_get_system_metrics":
            metric = arguments.get("metric_type", "cpu")
            return {"status": "healthy", "value": "24%", "metric": metric}
            
        return {"error": "Unknown tool requested"}

class MCPTool(BaseTool):
    """
    A specialized ADK tool that wraps an MCP discovered tool.
    Explicitly provides the parameter schema to the LLM.
    """
    def __init__(self, client: MCPClient, tool_def: Dict[str, Any]):
        super().__init__(
            name=tool_def["name"],
            description=tool_def["description"]
        )
        self.client = client
        self.tool_def = tool_def

    def _get_declaration(self) -> Optional[types.FunctionDeclaration]:
        # Convert the MCP 'parameters' dict (JSON Schema) into ADK's expected Schema format
        params_schema = types.Schema.model_validate(self.tool_def["parameters"])
        return types.FunctionDeclaration(
            name=self.name,
            description=self.description,
            parameters=params_schema
        )

    async def run_async(self, *, args: Dict[str, Any], tool_context: ToolContext) -> Any:
        return self.client.call_tool(self.name, args)

def get_mcp_tools(server_url: str = "http://mcp-server:8080") -> List[BaseTool]:
    """
    Factory function to discover MCP tools and wrap them as ADK MCPTools.
    """
    client = MCPClient(server_url)
    client.connect()
    
    adk_tools = []
    
    # Dynamically create wrappers for discovered tools
    for tool_def in client.list_tools():
        adk_tools.append(MCPTool(client, tool_def))
        
    return adk_tools

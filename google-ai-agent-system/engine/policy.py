from typing import Any, Dict, Optional, List
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.adk.models.llm_request import LlmRequest
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.base_agent import BaseAgent
from google.genai import types
from engine.identity import get_user_identity, check_permission

class AgentPolicyPlugin(BasePlugin):
    """
    Enterprise Policy Plugin to enforce Identity-based Human-in-the-loop (HITL) 
    and safety guardrails on tool execution.
    """
    def __init__(self, sensitive_tools: List[str]):
        super().__init__(name="agent_policy_enforcement")
        self.sensitive_tools = sensitive_tools

    async def before_agent_callback(self, *, agent: BaseAgent, callback_context: CallbackContext) -> Optional[Any]:
        # Inject identity into the session state if not already there
        user_id = callback_context.user_id
        identity = get_user_identity(user_id)
        
        # Store for retrieval in other callbacks
        callback_context.state["user_role"] = identity.role
        callback_context.state["username"] = identity.username
        return None

    async def before_tool_callback(
        self, 
        *, 
        tool: BaseTool, 
        tool_args: Dict[str, Any], 
        tool_context: ToolContext
    ) -> Optional[Dict]:
        """
        Intercept tool calls based on verified identity and permissions.
        """
        user_id = tool_context.user_id
        identity = get_user_identity(user_id)
        
        if tool.name in self.sensitive_tools:
            print(f"[POLICY] Intercepted sensitive tool: {tool.name} for user: {identity.username} ({identity.role})")
            
            # RBAC: 'mcp_read_document' requires 'read_internal' permission
            if tool.name == "mcp_read_document" and not check_permission(identity, "read_internal"):
                return {"error": f"SECURITY_BLOCK: User '{identity.username}' does not have the required 'read_internal' permission to use {tool.name}. Access Denied."}
            
            # Block 'write' level access for non-admins
            if tool_args.get("access_level") == "write" and identity.role != "admin":
                 return {"error": f"SECURITY_BLOCK: 'write' access to {tool.name} is restricted to Administrators only. User '{identity.username}' is unauthorized."}
        
        return None

    async def before_model_callback(
        self, 
        *, 
        callback_context: Any, 
        llm_request: LlmRequest
    ) -> Optional[Any]:
        """
        Inject identity-aware constraints.
        """
        user_id = callback_context.user_id
        identity = get_user_identity(user_id)
        
        policy_instruction = (
            f"\n\n[IDENTITY CONTEXT]: You are currently assisting {identity.username} (Role: {identity.role}). "
            "Tailor your responses to their technical level and clearance. "
            "Never disclose administrative credentials or bypass internal document IDs."
        )
        
        if llm_request.config.system_instruction:
            llm_request.config.system_instruction += policy_instruction
        else:
            llm_request.config.system_instruction = policy_instruction
            
        return None

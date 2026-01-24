from typing import Any, Dict, Optional, List
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.adk.models.llm_request import LlmRequest
from google.genai import types

class AgentPolicyPlugin(BasePlugin):
    """
    Enterprise Policy Plugin to enforce Human-in-the-loop (HITL) 
    and safety guardrails on tool execution.
    """
    def __init__(self, sensitive_tools: List[str]):
        super().__init__(name="agent_policy_enforcement")
        self.sensitive_tools = sensitive_tools

    async def before_tool_callback(
        self, 
        *, 
        tool: BaseTool, 
        tool_args: Dict[str, Any], 
        tool_context: ToolContext
    ) -> Optional[Dict]:
        """
        Intercept tool calls. If they are in the 'sensitive' list, 
        we could simulate a requirement for higher-level authorization 
        or simply log a compliance warning.
        
        In a full ADK implementation with ToolConfirmation, we would yield 
        a confirmation request here. For this demo, we add a policy metadata 
        to the tool result or block unauthorized access.
        """
        if tool.name in self.sensitive_tools:
            print(f"[POLICY] Intercepted sensitive tool: {tool.name}")
            # Example: Block access if a specific flag is missing (simulated)
            if tool_args.get("access_level") == "write" and not tool_args.get("authorized"):
                return {"error": f"Policy Violation: 'write' access to {tool.name} requires explicit manager authorization."}
        
        return None

    async def before_model_callback(
        self, 
        *, 
        callback_context: Any, 
        llm_request: LlmRequest
    ) -> Optional[Any]:
        """
        Inject global safety instructions or 'Company Policy' into the system prompt 
        dynamically before every model call.
        """
        policy_instruction = "\n\n[ENTERPRISE POLICY]: Always protect PII. Never disclose internal document IDs to external search results."
        
        if llm_request.config.system_instruction:
            llm_request.config.system_instruction += policy_instruction
        else:
            llm_request.config.system_instruction = policy_instruction
            
        return None

import logging
import time
from typing import Dict, Any, List, Optional
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.agents.base_agent import BaseAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.adk.models.llm_response import LlmResponse
from google.adk.models.llm_request import LlmRequest

# Configure basic logging to file
logging.basicConfig(
    filename='agent_trace.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("EnterpriseMonitor")

class EnterpriseObservabilityPlugin(BasePlugin):
    """
    ADK Plugin for deep observability and tracing.
    Mimics Google Cloud Operations suite by logging critical agent lifecycle events.
    """
    def __init__(self):
        super().__init__(name="enterprise_monitor")

    async def before_agent_callback(self, *, agent: BaseAgent, callback_context: CallbackContext) -> Optional[Any]:
        logger.info(f"[Agent:{agent.name}] Invocation started. Session: {callback_context.session.id}")
        return None

    async def after_agent_callback(self, *, agent: BaseAgent, callback_context: CallbackContext) -> Optional[Any]:
        logger.info(f"[Agent:{agent.name}] Invocation completed.")
        return None

    async def before_tool_callback(self, *, tool: BaseTool, tool_args: Dict[str, Any], tool_context: ToolContext) -> Optional[Dict]:
        logger.info(f"[Tool:{tool.name}] Starting execution with args: {tool_args}")
        return None

    async def after_tool_callback(self, *, tool: BaseTool, tool_args: Dict[str, Any], tool_context: ToolContext, result: Dict) -> Optional[Dict]:
        # Truncate result for logs
        res_str = str(result)[:200]
        logger.info(f"[Tool:{tool.name}] Completed. Result: {res_str}...")
        return None

    async def after_model_callback(self, *, callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
        usage = llm_response.usage_metadata if hasattr(llm_response, 'usage_metadata') else "N/A"
        logger.info(f"[LLM] Model responded. Usage: {usage}")
        return None

    async def on_tool_error_callback(self, *, tool: BaseTool, tool_args: Dict[str, Any], tool_context: ToolContext, error: Exception) -> Optional[Dict]:
        logger.error(f"[Tool:{tool.name}] FAILED with error: {str(error)}")
        return None

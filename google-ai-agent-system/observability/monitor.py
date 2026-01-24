import logging
import time
from langchain_core.callbacks import BaseCallbackHandler
from typing import Dict, Any, List

# Configure basic logging
logging.basicConfig(
    filename='agent_trace.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("AgentObservability")

class ObservabilityCallbackHandler(BaseCallbackHandler):
    """
    Custom Callback Handler to simulate Cloud Trace and Logging.
    In a real scenario, this would push data to Google Cloud Trace/Logging.
    """
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        logger.info(f"event=LLM_START model={serialized.get('kwargs', {}).get('model_name')} prompts={len(prompts)}")

    def on_llm_end(self, response: Any, **kwargs: Any) -> None:
        logger.info(f"event=LLM_END")

    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs: Any) -> None:
        logger.info(f"event=TOOL_START tool={serialized.get('name')} input={input_str}")

    def on_tool_end(self, output: Any, **kwargs: Any) -> None:
        try:
            if isinstance(output, str):
                log_msg = output[:50]
            elif hasattr(output, 'content'):
                log_msg = str(output.content)[:50]
            else:
                log_msg = str(output)[:50]
            logger.info(f"event=TOOL_END output={log_msg}...")
        except Exception as e:
            logger.error(f"event=TOOL_END error_parsing_output={e}")

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        logger.info(f"event=CHAIN_START inputs={list(inputs.keys())}")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        logger.info(f"event=CHAIN_END")

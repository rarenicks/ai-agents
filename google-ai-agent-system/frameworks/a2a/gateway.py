import asyncio
import logging
from typing import Dict, Any, List, Optional, Callable
from frameworks.a2a.protocol import A2AMessage, A2AMessageType, A2AContext
import time

logger = logging.getLogger("A2A_Dispatcher")

class A2AGateway:
    """
    The A2A Open Protocol Gateway.
    Manages communication for a fleet of autonomous agents.
    """
    def __init__(self):
        self._registry: Dict[str, Callable[[A2AMessage], Any]] = {}
        self._message_history: List[A2AMessage] = []

    def register_endpoint(self, agent_uri: str, callback: Callable):
        """Register an agent endpoint to receive A2A messages."""
        self._registry[agent_uri] = callback
        logger.info(f"[A2A] Agent endpoint registered: {agent_uri}")

    async def dispatch(self, message: A2AMessage) -> Optional[A2AMessage]:
        """Route an A2A message to its destination."""
        self._message_history.append(message)
        
        print(f"[A2A Dispatch] {message.type.upper()}: {message.sender} -> {message.receiver}")
        
        if message.receiver not in self._registry:
            logger.warning(f"[A2A] Receiver not found: {message.receiver}")
            return A2AMessage(
                sender="system://gateway",
                receiver=message.sender,
                type=A2AMessageType.ERROR,
                content=f"Routing Error: Agent {message.receiver} is unreachable.",
                context=A2AContext(trace_id=message.context.trace_id)
            )

        try:
            # Simulate network latency
            await asyncio.sleep(0.1)
            response = await self._registry[message.receiver](message)
            return response
        except Exception as e:
            logger.error(f"[A2A] Dispatch error: {e}")
            return None

    def get_system_topology(self) -> List[str]:
        """Return a list of all active agent endpoints in the A2A mesh."""
        return list(self._registry.keys())

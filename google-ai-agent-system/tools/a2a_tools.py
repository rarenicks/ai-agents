from typing import Any, Dict, List
import asyncio
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from frameworks.a2a.protocol import A2AMessage, A2AMessageType, A2AContext
from frameworks.a2a.gateway import A2AGateway

# Global Gateway instance (Simulated service mesh)
A2A_NET = A2AGateway()

async def mock_remote_finance_agent(message: A2AMessage) -> A2AMessage:
    """A simulated external agent using A2A protocol."""
    if message.type == A2AMessageType.DISCOVERY:
        return A2AMessage(
            sender=message.receiver,
            receiver=message.sender,
            type=A2AMessageType.RESULT,
            content="Capabilities: budget_analysis, tax_forecasting, portfolio_optimization.",
            context=A2AContext(trace_id=message.context.trace_id)
        )
    return A2AMessage(
        sender=message.receiver,
        receiver=message.sender,
        type=A2AMessageType.RESULT,
        content=f"Finance analysis for '{message.content}' completed. Status: Profit expected.",
        context=A2AContext(trace_id=message.context.trace_id)
    )

# Register the remote agent in our local mesh
A2A_NET.register_endpoint("agent://finance_remote", mock_remote_finance_agent)

def open_a2a_communication(recipient: str, task_text: str, msg_type: str = "task_assign") -> str:
    """
    Open an A2A protocol channel to a remote agent.
    
    Args:
        recipient: The A2A URI of the target agent (e.g., 'agent://finance_remote').
        task_text: The payload or command.
        msg_type: The A2A message type (discovery, task_assign, handoff).
    """
    # Note: ADK prefers sync functions for simple tools, but we wrap the async dispatch
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    msg = A2AMessage(
        sender="agent://supervisor",
        receiver=recipient,
        type=A2AMessageType(msg_type),
        content=task_text
    )
    
    # Run the async dispatch in a synchronous-looking way for the agent
    print(f"[A2A Tool] Opening channel to {recipient}...")
    
    # For safety in varied environments, we check if loop is running
    if loop.is_running():
        # This is a bit tricky in async environments, but for ADK sync tools:
        # In real world, A2A would be an async tool.
        return f"[A2A Tool] Deferred: A2A Request to {recipient} sent to mesh."
    
    response = loop.run_until_complete(A2A_NET.dispatch(msg))
    
    if response:
        return f"[A2A Protocol Result] {response.sender}: {response.content}"
    return "[A2A Protocol Error] Failed to receive response from remote agent."

def list_a2a_directory() -> str:
    """Retrieve the list of active agents in the A2A Open Directory."""
    endpoints = A2A_NET.get_system_topology()
    return "Active A2A Agent Registry: " + ", ".join(endpoints)

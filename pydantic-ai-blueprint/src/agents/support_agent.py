from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
from src.models.support import SupportResponse
from config.settings import settings

@dataclass
class SupportDeps:
    """Dependencies for the support agent."""
    customer_id: str
    tier: str

# Define the agent with a specific output model
support_agent = Agent(
    settings.OPENAI_MODEL_NAME,
    deps_type=SupportDeps,
    output_type=SupportResponse,
    system_prompt='''You are a premium support assistant for a cloud platform. 
    Use the customer tier to decide how empathetic or direct to be.
    If the user has a technical issue, suggest a basic fix.
    If you cannot resolve it, set status to 'escalated'.'''
)

@support_agent.tool
async def get_system_status(ctx: RunContext[SupportDeps]) -> str:
    """Check the current system status."""
    # In a real app, you'd use ctx.deps to check specific region status etc.
    return "All systems operational"

@support_agent.tool
async def check_last_bill(ctx: RunContext[SupportDeps]) -> str:
    """Check the customer's last bill status."""
    if ctx.deps.customer_id == "42":
        return "Last bill: $12.00 (Paid)"
    return "Last bill not found"

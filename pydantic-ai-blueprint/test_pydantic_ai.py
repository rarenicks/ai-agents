import asyncio
import logfire
from logfire import AdvancedOptions
from src.agents.support_agent import support_agent, SupportDeps
from config.settings import settings

# Configure logfire for the test
logfire.configure(
    service_name="ai-agents",
    token=settings.LOGFIRE_TOKEN,
    advanced=AdvancedOptions(base_url=settings.LOGFIRE_BASE_URL)
)

async def main():
    print(f"Testing PydanticAI with model: {settings.OPENAI_MODEL_NAME}")
    
    # Dependencies
    deps = SupportDeps(customer_id="42", tier="premium")
    
    # User Query
    query = "What was my last bill and is the system down?"
    print(f"\nUser: {query}")
    
    # Run Agent
    result = await support_agent.run(query, deps=deps)
    
    print("\n--- Agent Response ---")
    print(f"Status: {result.output.status}")
    print(f"Message: {result.output.message}")
    print(f"Reasoning: {result.output.reasoning}")

if __name__ == "__main__":
    asyncio.run(main())

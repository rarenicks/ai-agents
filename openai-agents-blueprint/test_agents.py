import asyncio
from src.workflows.runner import AgentOrchestrator
from config.settings import settings

async def main():
    print(f"Using model: {settings.OPENAI_MODEL_NAME}")
    orchestrator = AgentOrchestrator()
    
    # Minimal test query
    query = "Hi, I have a billing question."
    print(f"\nUser: {query}")
    
    result = await orchestrator.run_query(query)
    print(f"Agent Response: {result}")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from src.workflows.runner import AgentOrchestrator
from config.settings import settings

async def main():
    print(f"Using model: {settings.OPENAI_MODEL_NAME}")
    orchestrator = AgentOrchestrator()
    
    # This query should trigger Triage -> TechnicalAgent
    query = "I cannot connect to the database, help me."
    print(f"\nUser: {query}")
    
    result = await orchestrator.run_query(query)
    print(f"Agent Response: {result}")

if __name__ == "__main__":
    asyncio.run(main())

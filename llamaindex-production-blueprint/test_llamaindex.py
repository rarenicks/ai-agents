from src.agents.policy_agent import get_agent
import asyncio

async def main():
    print("Initializing LlamaIndex Policy Agent...")
    agent = get_agent()
    
    query = "What is the equipment stipend for remote work?"
    print(f"\nUser: {query}")
    
    # New LlamaIndex Workflow agents use .run() and need to be awaited
    result = await agent.run(user_msg=query)
    print(f"\nAgent: {str(result)}")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from src.agents.research_graph import research_graph

async def main():
    print("Testing LangGraph Research Graph...")
    
    config = {"configurable": {"thread_id": "test-thread"}}
    
    initial_state = {
        "messages": [{"role": "user", "content": "What are the top 3 benefits of using LangGraph for agent orchestration?"}],
        "research": "",
        "critic_loops": 0,
        "is_complete": False
    }
    
    print("\nRunning graph...")
    async for event in research_graph.astream(initial_state, config=config, stream_mode="values"):
        messages = event.get("messages", [])
        if messages:
            latest_msg = messages[-1]
            if latest_msg["role"] == "assistant":
                print(f"\n[Agent]: {latest_msg['content']}")
        
        if event.get("is_complete") or event.get("critic_loops", 0) >= 2:
            print("\n--- Final Research Result ---")
            print(event["research"])
            break

if __name__ == "__main__":
    asyncio.run(main())

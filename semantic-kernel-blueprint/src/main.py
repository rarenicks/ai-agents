import asyncio
import sys
import os

# Set Python Path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestration.workflow import run_enterprise_workflow

async def main():
    print("🔮 Semantic Kernel Blueprint")
    print("---------------------------------------")
    
    query = "Analyze the impact of Agentic Workflows on Enterprise Productivity."
    print(f"User Query: {query}\n")
    
    try:
        result = await run_enterprise_workflow(query)
        print(f"\n✨ Final Result:\n{result}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())

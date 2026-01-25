import sys
import os

# Add root to path so we can import from src and config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.workflows.team_orchestration import ResearchTeam

def main():
    print("🚀 Starting AutoGen Research Team...")
    team = ResearchTeam()
    
    topic = "The impact of Agentic Workflows on Enterprise Productivity"
    print(f"Topic: {topic}\n")
    
    result = team.run(f"Please analyze the following topic and provide a critical review: {topic}. End your final response with TERMINATE.")
    print(f"\n✨ Final Result:\n{result}")

if __name__ == "__main__":
    main()

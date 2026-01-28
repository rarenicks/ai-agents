from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from config.settings import settings
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_agent():
    print("Testing Agno Agent...")
    
    agent = Agent(
        model=OpenAIChat(id=settings.openai_model_name, api_key=settings.openai_api_key),
        tools=[DuckDuckGoTools()],
        instructions=["Always provide concise, one-liner answers to save token usage."],
        markdown=True
    )
    
    print("\nQuerying: What is the current weather in New York?")
    response = agent.run("What is the current weather in New York?", stream=False)
    
    # Agno run returns a RunResponse object
    content = response.content if hasattr(response, 'content') else str(response)
    print(f"\nResponse: {content}")

if __name__ == "__main__":
    test_agent()

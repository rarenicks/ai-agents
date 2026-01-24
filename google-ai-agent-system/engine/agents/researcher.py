import os
from google.adk.agents.llm_agent import Agent
from tools.search_tool import web_search

def build_researcher():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()
    
    # ADK uses a specific Agent class that encapsulates instruction and tools
    researcher = Agent(
        model=model_name,
        name="Senior_Researcher", # Standardized name
        description="Expert at gathering and synthesizing information from the web.",
        instruction="""You are a Senior Researcher. 
        Your role is to gather thorough information on a given topic using your search tools.
        Be precise, factual, and cite your sources.""",
        tools=[web_search],
    )
    
    return researcher


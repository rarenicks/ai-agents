import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools.basic_tools import calculate_length, get_weather
from tools.search_tool import web_search

def build_agent():
    # Ensure GOOGLE_API_KEY or GOOGLE_APPLICATION_CREDENTIALS is set
    # implementing a fallback or mock for learning purposes if creds are missing is tricky,
    # allows 'mock' behavior if desired, but here we assume standard setup.
    
    # We will use the centralized LLM factory (handles Mock Mode)
    from engine.llm_factory import get_llm
    llm = get_llm(model_name="gemini-1.5-flash")
    
    tools = [calculate_length, get_weather, web_search]
    
    # Create a prebuilt ReAct agent using LangGraph
    agent_executor = create_react_agent(llm, tools)
    
    return agent_executor

import os
from google.adk.agents.llm_agent import Agent
from tools.search_tool import web_search

def build_researcher():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()
    
    # Discover Enterprise tools via MCP
    from frameworks.mcp.client import get_mcp_tools
    mcp_tools = get_mcp_tools()

    # ADK uses a specific Agent class that encapsulates instruction and tools
    researcher = Agent(
        model=model_name,
        name="Senior_Researcher", # Standardized name
        description="Expert at gathering and synthesizing information from the web and internal enterprise docs via MCP.",
        instruction="""You are a Senior Researcher. 
        Your role is to gather thorough information on a given topic using your search tools.
        You also have access to internal enterprise documents via MCP tools.
        Be precise, factual, and cite your sources. 
        IMPORTANT: If you use an MCP tool and it returns a SECURITY_BLOCK or an error, you MUST report this exact reason to the user immediately. Do not attempt to bypass or ignore security denials.""",
        tools=[web_search] + mcp_tools,
    )
    
    return researcher


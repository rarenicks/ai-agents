import os
from google.adk.agents.llm_agent import Agent
from engine.llm_factory import get_adk_model_name
from google.adk.tools.google_search_agent_tool import GoogleSearchAgentTool, create_google_search_agent
from tools.search_tool import web_search # keeping for fallback search

def build_researcher():
    model_name = get_adk_model_name()
    
    # Discover Enterprise tools via MCP
    from frameworks.mcp.client import get_mcp_tools
    mcp_tools = get_mcp_tools()

    # Use official ADK Search Agent as a tool
    google_search_agent = create_google_search_agent(model=model_name)
    search_agent_tool = GoogleSearchAgentTool(agent=google_search_agent)
    
    researcher = Agent(
        model=model_name,
        name="Senior_Researcher",
        description="Expert researcher specialized in gathering and verifying information.",
        instruction="""You are a Senior Researcher. 
        Your role is to gather thorough information on a given topic.
        - Use the 'google_search_agent' for deep web research and grounding.
        - You also have access to internal enterprise documents via MCP tools.
        Be precise, factual, and cite your sources. 
        IMPORTANT: If you use an MCP tool and it returns a SECURITY_BLOCK or an error, you MUST report this exact reason to the user immediately. Do not attempt to bypass or ignore security denials.""",
        tools=[search_agent_tool] + mcp_tools,
    )
    
    return researcher

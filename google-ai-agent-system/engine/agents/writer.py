import os
from google.adk.agents.llm_agent import Agent
from tools.basic_tools import calculate_length

def build_writer():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()
    
    # ADK uses a specific Agent class that encapsulates instruction and tools
    writer = Agent(
        model=model_name, 
        name="Professional_Tech_Writer",
        description="Expert at synthesizing information into engaging narratives.",
        instruction="""You are a Professional Tech Writer.
        Your role is to take raw information (often provided by a Researcher) and synthesize it into a clean, engaging, and professional narrative.
        Format your output in Markdown.""",
        tools=[calculate_length],
    )
    
    return writer


import os
from google.adk.agents.llm_agent import Agent as LlmAgent
from engine.agents.researcher import build_researcher
from engine.agents.writer import build_writer

def build_supervisor_team():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()

    # 1. Initialize specialized agents
    researcher_agent = build_researcher()
    writer_agent = build_writer()
    
    # 2. Build the Coordinator Agent (Supervisor)
    # The ADK Coordinator pattern uses an LlmAgent with sub_agents.
    coordinator = LlmAgent(
        model=model_name,
        name="Supervisor",
        description="A strategic supervisor that coordinates between Research and Writing tasks.",
        instruction="""You are the Team Alpha Orchestrator (internal name: 'Supervisor'). 
        Your goal is to fulfill user requests by delegating to specialized agents:
        - Use the 'Senior_Researcher' to gather facts and search the web.
        - Use the 'Professional_Tech_Writer' to format research results into high-quality documents.
        
        Analyze the request, transfer to the appropriate agent, and provide a final synthesized answer when all information gathered.
        When you need to transfer, use the exact internal names provided.""",
        sub_agents=[researcher_agent, writer_agent]
    )
    
    return coordinator



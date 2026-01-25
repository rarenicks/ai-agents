from autogen import AssistantAgent, UserProxyAgent
from config.settings import settings

def create_analyst_agent():
    return AssistantAgent(
        name="Analyst",
        system_message="""You are a Senior Strategic Analyst. 
        Your goal is to analyze data, identify patterns, and provide strategic recommendations.
        Always base your analysis on facts and be as precise as possible.
        BE EXTREMELY BRIEF (MAX 2 SENTENCES).""",
        llm_config=settings.llm_config,
    )

def create_critic_agent():
    return AssistantAgent(
        name="Critic",
        system_message="""You are a Critical Reviewer. 
        Your role is to challenge assumptions, identify potential risks, and ensure high-quality output.
        Focus on logic, feasibility, and potential downsides of any plan.
        BE EXTREMELY BRIEF (MAX 2 SENTENCES).""",
        llm_config=settings.llm_config,
    )

def create_user_proxy():
    return UserProxyAgent(
        name="Admin",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,  # Set to True for production
        },
    )

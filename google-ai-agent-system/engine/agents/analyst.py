from google.adk.agents.llm_agent import Agent
from google.adk.code_executors.unsafe_local_code_executor import UnsafeLocalCodeExecutor
from tools.basic_tools import calculate_length

def build_data_analyst():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()
    
    # ADK Code Executor allows the agent to run Python blocks found in its response
    code_executor = UnsafeLocalCodeExecutor()
    
    analyst = Agent(
        model=model_name,
        name="Data_Analyst",
        description="Expert at data analysis and Python programming. Can execute code to solve complex problems.",
        instruction="""You are an expert Data Analyst.
        When asked to perform calculations, data processing, or complex logic, you should write and execute Python code.
        Always explain your logic and show the results of your code execution.
        If a user asks for a visualization, describe how the data looks.""",
        code_executor=code_executor,
        tools=[calculate_length] # analyst can also use basic tools
    )
    
    return analyst

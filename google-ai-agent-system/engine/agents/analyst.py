from google.adk.agents.llm_agent import Agent
from google.adk.code_executors.unsafe_local_code_executor import UnsafeLocalCodeExecutor
from google.adk.tools.agent_tool import AgentTool
from tools.basic_tools import calculate_length

def build_data_analyst():
    from engine.llm_factory import get_adk_model_name
    model_name = get_adk_model_name()
    
    # 1. Create a specialized Code Interpreter Agent (Sub-Agent)
    code_interpreter_agent = Agent(
        model=model_name,
        name="code_interpreter",
        description="A specialized agent that writes and executes Python code to solve problems.",
        instruction="""You are a Python expert. 
        When you receive a logic, math, or data processing request, write a Python block and execute it.
        Provide only the code and its result back to the user.""",
        code_executor=UnsafeLocalCodeExecutor()
    )
    
    # 2. Wrap the sub-agent into a Tool
    code_interpreter_tool = AgentTool(agent=code_interpreter_agent)
    
    # 3. Use the Tool in our main Data Analyst
    analyst = Agent(
        model=model_name,
        name="Data_Analyst",
        description="Expert at data analysis. Uses specialized tools and sub-agents for computation.",
        instruction="""You are an expert Data Analyst.
        - For any complex calculation, prime number search, or data manipulation, delegate to the 'code_interpreter'.
        - Use your basic tools for simple metadata tasks.
        Explain the overall logic clearly after receiving the results.""",
        tools=[code_interpreter_tool, calculate_length]
    )
    
    return analyst

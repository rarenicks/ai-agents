from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.agents.strategies import TerminationStrategy
from semantic_kernel.agents.group_chat.agent_group_chat import AgentGroupChat
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.utils.author_role import AuthorRole

from config.settings import settings
from src.plugins.research_plugin import ResearchPlugin

class FinalApprovalTerminationStrategy(TerminationStrategy):
    """
    Terminates when the Reviewer gives approval or the word 'TERMINATE' is detected.
    """
    async def should_agent_terminate(self, agent, history):
        if history and "TERMINATE" in history[-1].content:
            return True
        return False

async def run_enterprise_workflow(query: str):
    # Setup Kernel
    kernel = settings.create_kernel()
    
    # Register Plugins
    kernel.add_plugin(ResearchPlugin(), plugin_name="Research")
    
    # Define Agents
    analyst = ChatCompletionAgent(
        kernel=kernel,
        name="Analyst",
        instructions="""You are a Senior Business Analyst. 
        Your goal is to gather facts using the Research plugin and propose a strategy.
        Be concise. Use maximum 2 sentences.
        Wait for the Reviewer's feedback.""",
    )
    
    reviewer = ChatCompletionAgent(
        kernel=kernel,
        name="Reviewer",
        instructions="""You are a Critical Reviewer. 
        Verify the Analyst's proposal. If it meets enterprise standards, say 'APPROVED. TERMINATE'.
        Otherwise, provide one brief critique.
        BE EXTREMELY BRIEF (MAX 2 SENTENCES).""",
    )
    
    # Group Chat Management
    chat = AgentGroupChat(
        agents=[analyst, reviewer],
        termination_strategy=FinalApprovalTerminationStrategy(maximum_iterations=4)
    )
    
    # Initiate Task
    await chat.add_chat_message(ChatMessageContent(role=AuthorRole.USER, content=query))
    
    # Execute and Stream Results
    final_output = ""
    async for message in chat.invoke():
        print(f"[{message.name}]: {message.content}")
        final_output = message.content
        
    return final_output

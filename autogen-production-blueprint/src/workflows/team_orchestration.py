from autogen import GroupChat, GroupChatManager
from src.agents.custom_agents import create_analyst_agent, create_critic_agent, create_user_proxy
from config.settings import settings

class ResearchTeam:
    def __init__(self):
        self.user_proxy = create_user_proxy()
        self.analyst = create_analyst_agent()
        self.critic = create_critic_agent()
        
    def run(self, message: str):
        groupchat = GroupChat(
            agents=[self.user_proxy, self.analyst, self.critic],
            messages=[],
            max_round=3
        )
        manager = GroupChatManager(groupchat=groupchat, llm_config=settings.llm_config)
        
        # Initiate the conversation
        self.user_proxy.initiate_chat(
            manager,
            message=message
        )
        
        # Return the last message from the group chat
        return groupchat.messages[-1]["content"] if groupchat.messages else "No response generated."

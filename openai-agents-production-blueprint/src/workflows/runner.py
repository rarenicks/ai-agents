from openai import AsyncOpenAI
from agents import Runner, set_default_openai_client
from src.agents.handoff_agents import create_triage_agent
from config.settings import settings

class AgentOrchestrator:
    def __init__(self):
        # Initialize the triage agent
        self.triage_agent = create_triage_agent()
        
        # Configure the global client for the SDK
        if settings.PROVIDER == "azure_openai":
            self.client = AsyncOpenAI(
                api_key=settings.AZURE_OPENAI_API_KEY,
                base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/deployments/{settings.AZURE_OPENAI_CHAT_DEPLOYMENT}",
            )
        else:
            self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        
        set_default_openai_client(self.client)

    async def run_query(self, user_input: str):
        # Use the Runner utility class
        result = await Runner.run(
            starting_agent=self.triage_agent,
            input=user_input
        )
        return str(result.final_output)

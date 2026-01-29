from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite.sqlite import SqliteDb
from config.settings import settings

def get_assistant(user_id: str = "default_user", session_id: str = None):
    """
    Returns an Agno Agent with tool-calling and storage.
    """
    return Agent(
        name="BlueprintAssistant",
        model=OpenAIChat(id=settings.openai_model_name, api_key=settings.openai_api_key),
        tools=[DuckDuckGoTools()],
        description="You are a helpful assistant that uses tools to answer questions.",
        instructions=[
            "Always provide concise, one-liner answers to save token usage.",
            "Use tools when necessary to find up-to-date information.",
        ],
        db=SqliteDb(
            session_table="agent_sessions",
            db_url=settings.db_url,
        ),
        add_history_to_context=True,
        num_history_runs=3,
        session_id=session_id,
        user_id=user_id,
        markdown=True,
    )

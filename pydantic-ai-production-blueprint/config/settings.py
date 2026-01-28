import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Model Provider: openai
    PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    
    # Optional: Logfire integration (PydanticAI's preferred observability tool)
    LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN")

settings = Settings()

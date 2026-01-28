import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Model Provider: openai
    PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    
    # Optional: Logfire integration
    LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN")
    LOGFIRE_BASE_URL = os.getenv("LOGFIRE_BASE_URL", "https://logfire-api.pydantic.dev")

settings = Settings()

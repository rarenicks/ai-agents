import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Model Provider: openai, azure_openai
    PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    
    # Azure Settings
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    @property
    def client_config(self):
        if self.PROVIDER == "azure_openai":
            return {
                "api_key": self.AZURE_OPENAI_API_KEY,
                "azure_endpoint": self.AZURE_OPENAI_ENDPOINT,
                "api_version": "2024-06-01",
                "azure_deployment": self.AZURE_OPENAI_CHAT_DEPLOYMENT
            }
        else:
            return {
                "api_key": self.OPENAI_API_KEY,
                "base_url": None
            }

settings = Settings()

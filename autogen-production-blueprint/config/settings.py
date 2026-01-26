import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Model Provider: openai, azure_openai (Default: openai)
    PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    
    # Azure Settings
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    @property
    def llm_config(self):
        config = {
            "cache_seed": 42,
            "temperature": 0,
        }
        
        if self.PROVIDER == "azure_openai":
            config["config_list"] = [
                {
                    "model": self.AZURE_OPENAI_CHAT_DEPLOYMENT,
                    "api_key": self.AZURE_OPENAI_API_KEY,
                    "base_url": self.AZURE_OPENAI_ENDPOINT,
                    "api_type": "azure",
                    "api_version": self.AZURE_OPENAI_API_VERSION,
                }
            ]
        else:
            config["config_list"] = [
                {
                    "model": self.OPENAI_MODEL_NAME,
                    "api_key": self.OPENAI_API_KEY,
                }
            ]
        return config

settings = Settings()

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    
    @property
    def llm_config(self):
        return {
            "config_list": [
                {
                    "model": self.MODEL_NAME,
                    "api_key": self.OPENAI_API_KEY,
                }
            ],
            "cache_seed": 42,  # For reproducibility
            "temperature": 0,
        }

settings = Settings()

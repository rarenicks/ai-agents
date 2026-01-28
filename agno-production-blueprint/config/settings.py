from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    openai_api_key: str
    openai_model_name: str = "gpt-4o-mini"
    
    # Storage settings (phidata specific)
    db_url: str = "sqlite:///agno.db"
    
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

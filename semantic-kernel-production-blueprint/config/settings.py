import os
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

load_dotenv()

class Settings:
    # Model Provider: ollama, openai, azure_openai
    PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
    
    # Ollama Settings
    OLLAMA_MODEL_ID = os.getenv("OLLAMA_MODEL_ID", "llama3.2")
    OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/v1")
    
    # OpenAI Settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_ID = os.getenv("OPENAI_MODEL_ID", "gpt-4o-mini")
    
    # Azure OpenAI Settings
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

    def create_kernel(self) -> Kernel:
        kernel = Kernel()
        
        if self.PROVIDER == "ollama":
            from openai import AsyncOpenAI
            # Use AsyncOpenAI client for Ollama's OpenAI-compatible endpoint
            client = AsyncOpenAI(
                api_key="ollama", # placeholder
                base_url=self.OLLAMA_ENDPOINT
            )
            kernel.add_service(
                OpenAIChatCompletion(
                    service_id="default",
                    ai_model_id=self.OLLAMA_MODEL_ID,
                    async_client=client
                )
            )
        elif self.PROVIDER == "openai":
            kernel.add_service(
                OpenAIChatCompletion(
                    service_id="default",
                    ai_model_id=self.OPENAI_MODEL_ID,
                    api_key=self.OPENAI_API_KEY
                )
            )
        elif self.PROVIDER == "azure_openai":
            kernel.add_service(
                AzureChatCompletion(
                    service_id="default",
                    deployment_name=self.AZURE_OPENAI_CHAT_DEPLOYMENT,
                    endpoint=self.AZURE_OPENAI_ENDPOINT,
                    api_key=self.AZURE_OPENAI_API_KEY
                )
            )
        else:
            raise ValueError(f"Unsupported provider: {self.PROVIDER}")
            
        return kernel

settings = Settings()

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from typing import Any, List, Optional
from langchain_core.outputs import ChatResult, ChatGeneration

class MockChatModel(BaseChatModel):
    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs: Any):
        last_msg = messages[-1].content.lower()
        all_text = " ".join([str(m.content).lower() for m in messages])
        
        response_text = "I am the AI Agent System. How can I help?"
        
        if "researcher" in all_text and "writer" in all_text and "next worker" in all_text:
            has_research = any("researcher" in str(msg.content).lower() for msg in messages if isinstance(msg, AIMessage))
            has_writer = any("writer" in str(msg.content).lower() for msg in messages if isinstance(msg, AIMessage))
            
            if not has_research:
                response_text = "Researcher"
            elif not has_writer:
                response_text = "Writer"
            else:
                response_text = "FINISH"
        elif "capital of france" in last_msg:
            response_text = "The capital of France is Paris."
        elif "australian open 2024" in last_msg:
            response_text = "Jannik Sinner won the Australian Open 2024 Men's Singles title."
        elif "google deepmind" in last_msg:
            response_text = "The length of 'Google DeepMind' is 15 characters."
        
        ai_message = AIMessage(content=response_text)
        return ChatResult(generations=[ChatGeneration(message=ai_message)])

    @property
    def _llm_type(self) -> str:
        return "mock-llm"

    def bind_tools(self, tools: List[Any], **kwargs: Any) -> Any:
        return self

def get_adk_model_name():
    if os.getenv("MOCK_AGENTS") == "True":
        # ADK doesn't have a direct Mock provider in the same way, 
        # but we can handle this in the agent setup if needed.
        # For now, return a placeholder or keep using the real one if mocks aren't implemented in ADK.
        return "gemini-1.5-flash"
    
    if os.getenv("USE_OLLAMA") == "True":
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
        return f"ollama/{ollama_model}"
    
    return os.getenv("GOOGLE_MODEL", "gemini-1.5-flash")

def get_llm(model_name: str = "llama3.2", max_tokens: int = 1024):
    if os.getenv("MOCK_AGENTS") == "True":
        return MockChatModel()
    
    # Check for Ollama preference
    if os.getenv("USE_OLLAMA") == "True":
        from langchain_ollama import ChatOllama
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
        print(f"[LLM Factory] Returning ChatOllama for {ollama_model}")
        return ChatOllama(model=ollama_model)

    # Fallback to Google AI Studio if Ollama is not enabled
    print(f"[LLM Factory] Returning ChatGoogleGenerativeAI for {model_name}")
    return ChatGoogleGenerativeAI(
        model=model_name,
        max_output_tokens=max_tokens
    )

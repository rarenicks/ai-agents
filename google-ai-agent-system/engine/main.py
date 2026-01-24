from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine.space.registry import AgentRegistry, AgentMetadata
from engine.agents.supervisor import build_supervisor_team
from engine.memory.store import MemoryStore
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.apps.app import App, ResumabilityConfig
from google.adk.agents.context_cache_config import ContextCacheConfig
from google.adk.models.registry import LLMRegistry
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
import os
from dotenv import load_dotenv
from observability.monitor import EnterpriseObservabilityPlugin
from engine.policy import AgentPolicyPlugin
import time

# Register Ollama support for ADK
LLMRegistry._register(r"ollama/.*", LiteLlm)

load_dotenv()

app = FastAPI(title="Google AI Agent System Engine")
memory = MemoryStore()
session_service = InMemorySessionService()
registry = AgentRegistry()

# ADK Core Components
try:
    # Build the root team
    team_alpha_agent = build_supervisor_team()
    
    # Create ADK App with Enterprise Features
    adk_app = App(
        name="Team_Alpha_App",
        root_agent=team_alpha_agent,
        plugins=[
            EnterpriseObservabilityPlugin(),
            AgentPolicyPlugin(sensitive_tools=["mcp_read_document"])
        ],
        resumability_config=ResumabilityConfig(is_resumable=True),
        context_cache_config=ContextCacheConfig(ttl_seconds=3600) # 1 hour TTL
    )
    
    # Initialize ADK Runner
    runner = Runner(
        app=adk_app,
        session_service=session_service,
        auto_create_session=True
    )
    
    # Register agents for discovery/dashboard
    registry.register("team_alpha", lambda: team_alpha_agent, AgentMetadata(
        name="Team Alpha Orchestrator",
        description="Strategic supervisor that plans and delegates tasks.",
        capabilities=["orchestration", "planning"]
    ))
    
    # Add a health check for the team
    registry.set_health_check("team_alpha", lambda: runner is not None)
    
    print("[Agentspace] ADK Runner initialized with Team Alpha.")
except Exception as e:
    import traceback
    print(f"[Agentspace] Error bootstrapping agents: {e}")
    traceback.print_exc()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/agent/chat")
async def chat(request: ChatRequest):
    try:
        # High-level tracking in our custom MemoryStore
        memory.add_message(request.session_id, "user", request.message)
        
        # Invoke ADK Runner
        new_msg = types.Content(
            role="user",
            parts=[types.Part(text=request.message)]
        )
        
        response_content = ""
        new_artifacts = []
        
        # Run the agent team within the ADK session
        async for event in runner.run_async(
            user_id="default_user",
            session_id=request.session_id,
            new_message=new_msg
        ):
            # Process ADK Events
            
            # Accumulate text from agent responses
            if event.author != "user" and event.content:
                if hasattr(event.content, 'parts'):
                    for part in event.content.parts:
                        if part.text:
                            response_content += part.text
            
            # Extract artifact metadata if provided
            if event.actions and event.actions.artifact_delta:
                new_artifacts.extend(event.actions.artifact_delta.keys())

        # Sync back to our MemoryStore
        if response_content:
            memory.add_message(request.session_id, "assistant", response_content)
        
        for art_name in new_artifacts:
            memory.add_artifact(request.session_id, {"id": art_name, "type": "adk_artifact"})
            
        return {
            "response": response_content,
            "history_count": len(memory.get_history(request.session_id)),
            "artifacts_count": len(memory.get_artifacts(request.session_id))
        }
            
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {
        "status": "running", 
        "agents": registry.list_agents(),
        "runner": "active",
        "timestamp": time.time()
    }

@app.get("/agent/health/check")
async def perform_health_check():
    results = registry.check_health()
    return {"results": results, "summary": registry.list_agents()}

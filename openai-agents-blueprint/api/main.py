from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.workflows.runner import AgentOrchestrator
import uvicorn
import os
import sys

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="OpenAI Agent SDK Production API", version="1.0.0")

class AgentRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    status: str
    result: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "framework": "openai-agents"}

@app.post("/chat", response_model=AgentResponse)
async def chat(request: AgentRequest):
    try:
        orchestrator = AgentOrchestrator()
        result = await orchestrator.run_query(request.query)
        return AgentResponse(status="success", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)

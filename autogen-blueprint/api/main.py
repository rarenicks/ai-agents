from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.workflows.team_orchestration import ResearchTeam
import uvicorn
import os
import sys

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="AutoGen Blueprint API", version="1.0.0")

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    status: str
    result: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "framework": "autogen"}

@app.post("/research", response_model=ResearchResponse)
async def perform_research(request: ResearchRequest):
    try:
        team = ResearchTeam()
        result = team.run(f"Please analyze the following topic and provide a critical review: {request.topic}. End your final response with TERMINATE.")
        return ResearchResponse(status="success", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

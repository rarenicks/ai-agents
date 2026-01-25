from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.crew import ProductionBlueprintCrew
import uvicorn

app = FastAPI(title="CrewAI Production API", version="1.0.0")

class KickoffRequest(BaseModel):
    topic: str

class KickoffResponse(BaseModel):
    status: str
    result: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "crewai-production-blueprint"}

@app.post("/kickoff", response_model=KickoffResponse)
async def kickoff_crew(request: KickoffRequest):
    try:
        inputs = {'topic': request.topic}
        result = ProductionBlueprintCrew().crew().kickoff(inputs=inputs)
        return KickoffResponse(status="success", result=str(result))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

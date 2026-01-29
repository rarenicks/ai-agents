from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.orchestration.workflow import run_enterprise_workflow
import uvicorn
import os
import sys

# Set Python Path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="Semantic Kernel Blueprint API", version="1.0.0")

class WorkflowRequest(BaseModel):
    query: str

class WorkflowResponse(BaseModel):
    status: str
    result: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "semantic-kernel-blueprint"}

@app.post("/run", response_model=WorkflowResponse)
async def run_workflow(request: WorkflowRequest):
    try:
        result = await run_enterprise_workflow(request.query)
        return WorkflowResponse(status="success", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)

import logfire
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents.support_agent import support_agent, SupportDeps
from src.models.support import SupportResponse
from config.settings import settings
import uvicorn
import os
import sys

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Logfire
if settings.LOGFIRE_TOKEN:
    logfire.configure(token=settings.LOGFIRE_TOKEN)
else:
    logfire.configure() # Open telemetry / console logging fallback

app = FastAPI(title="PydanticAI Production API", version="1.0.0")
logfire.instrument_fastapi(app)

class SupportRequest(BaseModel):
    customer_id: str
    query: str
    tier: str = "standard"

@app.get("/health")
def health_check():
    return {"status": "healthy", "framework": "pydantic-ai"}

@app.post("/support", response_model=SupportResponse)
async def handle_support(request: SupportRequest):
    try:
        # PydanticAI uses 'run' with dependencies
        deps = SupportDeps(customer_id=request.customer_id, tier=request.tier)
        result = await support_agent.run(request.query, deps=deps)
        
        # result.output will already be a SupportResponse instance
        return result.output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)

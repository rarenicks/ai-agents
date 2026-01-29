from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents.policy_agent import get_agent
import uvicorn
import os
import sys

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="LlamaIndex Production API", version="1.0.0")

# Cache the agent instance
agent = get_agent()

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "framework": "llamaindex"}

@app.post("/chat")
async def handle_chat(request: QueryRequest):
    try:
        response = await agent.run(user_msg=request.query)
        return {
            "response": str(response)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8006)

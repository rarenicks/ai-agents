from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents.research_graph import research_graph
from config.settings import settings
import uvicorn
import uuid
import sys
import os

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="LangGraph Production API", version="1.0.0")

class ChatRequest(BaseModel):
    query: str
    thread_id: str = str(uuid.uuid4())

@app.get("/health")
def health_check():
    return {"status": "healthy", "framework": "langgraph"}

@app.post("/research")
async def handle_research(request: ChatRequest):
    try:
        config = {"configurable": {"thread_id": request.thread_id}}
        
        # Initial state
        initial_state = {
            "messages": [{"role": "user", "content": request.query}],
            "research": "",
            "critic_loops": 0,
            "is_complete": False
        }
        
        final_state = await research_graph.ainvoke(initial_state, config=config)
        
        return {
            "thread_id": request.thread_id,
            "result": final_state["research"],
            "messages": final_state["messages"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from src.agents.assistant import get_assistant
import uuid

app = FastAPI(title="Phidata Production Agent API")

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    user_id: Optional[str] = "default_user"

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        session_id = request.session_id or str(uuid.uuid4())
        assistant = get_assistant(user_id=request.user_id, session_id=session_id)
        
        # Run the assistant and get response
        # Note: Assistant.run returns a generator or a string depending on stream
        response_gen = assistant.run(request.message, stream=False)
        
        # Phidata usually returns a RunResponse object if stream=False
        # In newer versions, it might just be the result or a RunResponse
        response_text = response_gen.content if hasattr(response_gen, 'content') else str(response_gen)
        
        return ChatResponse(
            response=response_text,
            session_id=session_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

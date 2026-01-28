from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.modules.fact_checker import get_module

app = FastAPI(title="DSPy Production Blueprint")

# Initialize the module once on startup
module = get_module()

class CheckRequest(BaseModel):
    context: str
    claim: str

class CheckResponse(BaseModel):
    reasoning: str
    assessment: str

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/check", response_model=CheckResponse)
async def check_claim(request: CheckRequest):
    try:
        # Call the DSPy module's forward pass
        prediction = module.forward(context=request.context, claim=request.claim)
        
        return CheckResponse(
            reasoning=prediction.reasoning,
            assessment=prediction.assessment
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from pydantic import BaseModel, Field

class SupportResponse(BaseModel):
    """Structured response for customer support."""
    status: str = Field(description="The status of the request: 'resolved' or 'escalated'")
    message: str = Field(description="The message to show to the customer")
    reasoning: str = Field(description="Brief internal reasoning for the response")

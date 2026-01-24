from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

class MessageType(str, Enum):
    REQUEST = "request"       # Initial task request
    HANDOFF = "handoff"       # Passing control/context to another agent
    UPDATE = "update"         # Intermediate status update
    FINAL_REPLY = "final_reply" # Completed task response
    ERROR = "error"           # Error reporting

class AgentArtifact(BaseModel):
    """Structured data produced by an agent that can be used by others."""
    id: str
    type: str  # e.g., "search_results", "draft", "metrics"
    data: Any
    timestamp: float

class AgentMessage(BaseModel):
    """
    A2A Open Protocol Message Format.
    Aligns with Google's vision for a common language between agents.
    """
    message_id: str = Field(..., description="Unique message ID")
    sender_id: str = Field(..., description="ID of the sending agent")
    recipient_id: str = Field(..., description="ID of the receiving agent")
    conversation_id: str = Field(..., description="Unique thread ID")
    
    type: MessageType = Field(default=MessageType.REQUEST)
    content: str = Field(..., description="The primary text/payload")
    
    artifacts: List[AgentArtifact] = Field(default_factory=list, description="Structured data shared in this message")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional context (e.g., source info, priority)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message_id": "msg-001",
                "sender_id": "supervisor",
                "recipient_id": "researcher",
                "conversation_id": "conv-456",
                "type": "handoff",
                "content": "Please research current AI trends.",
                "artifacts": [],
                "metadata": {"source": "user-request"}
            }
        }


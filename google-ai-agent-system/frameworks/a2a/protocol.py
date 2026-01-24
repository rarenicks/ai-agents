from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import uuid
import time

class A2AMessageType(str, Enum):
    # Core lifecycle
    DISCOVERY = "discovery"      # Find agent capabilities
    NEGOTIATION = "negotiation"  # Agree on task parameters/cost
    TASK_ASSIGN = "task_assign"  # Execute a specific action
    
    # Execution
    PROPOSAL = "proposal"        # Agent suggesting a plan
    OBSERVATION = "observation"  # Sharing environment data
    HANDOFF = "handoff"          # Transferring total control
    
    # Completion
    ACKNOWLEDGEMENT = "ack"      # Confirming receipt
    RESULT = "result"            # Final output delivery
    ERROR = "error"              # Failure notification

class A2AContext(BaseModel):
    """Contextual metadata for the A2A conversation."""
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    priority: int = 1  # 1-5, 5 being critical
    ttl: int = 3600    # Message validity in seconds
    security_level: str = "standard" # standard, confidential, restricted

class A2AArtifact(BaseModel):
    """Structured data shared between A2A agents."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    mimetype: str  # e.g., "application/json", "text/markdown"
    payload: Any
    schema_url: Optional[str] = None

class A2AMessage(BaseModel):
    """
    A2A (Autonomous Agent-to-Agent) Open Protocol.
    The next-generation standard for multi-agent synchronization.
    """
    protocol_version: str = "2.0.0"
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = Field(default_factory=time.time)
    
    sender: str = Field(..., description="URI or ID of the sender")
    receiver: str = Field(..., description="URI or ID of the receiver")
    
    type: A2AMessageType
    content: str
    
    context: A2AContext = Field(default_factory=A2AContext)
    artifacts: List[A2AArtifact] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_schema_extra = {
            "example": {
                "sender": "agent://supervisor",
                "receiver": "agent://researcher",
                "type": "task_assign",
                "content": "Analyze the impact of A2A on agent performance.",
                "context": {"priority": 3},
                "artifacts": []
            }
        }

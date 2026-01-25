from typing import Dict, Callable, Any, List, Optional
import time
from dataclasses import dataclass, field

@dataclass
class AgentMetadata:
    name: str
    description: str
    capabilities: List[str] = field(default_factory=list)
    version: str = "1.0.0"
    status: str = "ready" # New field for health status
    last_checked: float = field(default_factory=time.time)

class AgentRegistry:
    """
    Agentspace Registry: Manages the lifecycle and discovery of agents.
    """
    def __init__(self):
        self._agents: Dict[str, Callable] = {}
        self._metadata: Dict[str, AgentMetadata] = {}
        self._instances: Dict[str, Any] = {}
        self._health_checks: Dict[str, Callable[[], bool]] = {}

    def register(self, name: str, builder_func: Callable, metadata: Optional[AgentMetadata] = None):
        """Register a new agent with optional metadata."""
        print(f"[Agentspace] Registering agent: {name}")
        self._agents[name] = builder_func
        if metadata:
            self._metadata[name] = metadata
        else:
            # Fallback metadata
            self._metadata[name] = AgentMetadata(name=name, description="Core System Agent")

    def get_agent(self, name: str):
        """Get or lazily initialize an agent instance."""
        if name not in self._agents:
            raise ValueError(f"Agent '{name}' not found in Agentspace.")
        
        if name not in self._instances:
            print(f"[Agentspace] Initializing agent: {name}")
            self._instances[name] = self._agents[name]()
            
        return self._instances[name]

    def find_by_capability(self, capability: str) -> List[str]:
        """Discovery: Find agents that support a specific capability."""
        matches = []
        for name, meta in self._metadata.items():
            if capability in meta.capabilities:
                matches.append(name)
        return matches

    def get_metadata(self, name: str) -> Optional[AgentMetadata]:
        return self._metadata.get(name)

    def list_agents(self):
        return [
            {
                "id": name, 
                "name": meta.name, 
                "description": meta.description, 
                "status": meta.status,
                "capabilities": meta.capabilities
            }
            for name, meta in self._metadata.items()
        ]

    def update_status(self, name: str, status: str):
        if name in self._metadata:
            self._metadata[name].status = status
            self._metadata[name].last_checked = time.time()
            
    def set_health_check(self, name: str, check_func: Callable[[], bool]):
        self._health_checks[name] = check_func

    def check_health(self):
        results = {}
        for name, check_func in self._health_checks.items():
            try:
                is_healthy = check_func()
                status = "ready" if is_healthy else "degraded"
                self.update_status(name, status)
                results[name] = status
            except Exception:
                self.update_status(name, "error")
                results[name] = "error"
        return results

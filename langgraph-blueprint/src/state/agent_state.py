from typing import TypedDict, Annotated, List
import operator

class AgentState(TypedDict):
    """The state of the graph."""
    messages: Annotated[List[dict], operator.add]
    research: str
    critic_loops: int
    is_complete: bool

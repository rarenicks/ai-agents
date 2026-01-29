from typing import Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from src.state.agent_state import AgentState
from config.settings import settings

# Initialize the model
model = ChatOpenAI(model=settings.OPENAI_MODEL_NAME, api_key=settings.OPENAI_API_KEY)

# --- Nodes ---

async def researcher_node(state: AgentState):
    """Researches the topic concisely."""
    query = state["messages"][-1]["content"]
    response = await model.ainvoke(f"Research this topic and provide a 1-2 line summary ONLY: {query}")
    return {
        "messages": [{"role": "assistant", "content": response.content}],
        "research": response.content,
        "critic_loops": state.get("critic_loops", 0) + 1
    }

async def critic_node(state: AgentState):
    """Critiques the research concisely."""
    research = state["research"]
    response = await model.ainvoke(f"Critique this research (max 1 line). If perfect, say 'COMPLETE': {research}")
    
    is_complete = "COMPLETE" in response.content.upper()
    return {
        "messages": [{"role": "assistant", "content": response.content}],
        "is_complete": is_complete
    }

# --- Router ---

def router(state: AgentState) -> Literal["critic", "complete"]:
    """Decides whether to continue or end."""
    if state["is_complete"] or state["critic_loops"] >= 2:
        return "complete"
    return "critic"

# --- Build the Graph ---

workflow = StateGraph(AgentState)

workflow.add_node("researcher", researcher_node)
workflow.add_node("critic", critic_node)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "critic")

workflow.add_conditional_edges(
    "critic",
    router,
    {
        "critic": "researcher",
        "complete": END
    }
)

from langgraph.checkpoint.memory import MemorySaver

# Persistence (In-memory for stability)
memory = MemorySaver()

# Compile the graph
research_graph = workflow.compile(checkpointer=memory)

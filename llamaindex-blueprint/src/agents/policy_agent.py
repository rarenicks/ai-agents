from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from config.settings import settings
import os

# Initialize the LLM
llm = OpenAI(model=settings.OPENAI_MODEL_NAME, api_key=settings.OPENAI_API_KEY)

def get_agent():
    # 1. Load Data and Create Index
    reader = SimpleDirectoryReader(input_dir=settings.DATA_DIR)
    documents = reader.load_data()
    
    # In a real app, you'd use a Vector DB like Pinecone/Milvus here.
    # For the blueprint, we'll use a local simple vector index.
    index = VectorStoreIndex.from_documents(documents)
    
    # 2. Setup Query Engine as a Tool
    query_engine = index.as_query_engine(llm=llm)
    
    tools = [
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name="company_policy",
                description="Provides information about company remote work and reimbursement policies.",
            ),
        )
    ]
    
    # 3. Initialize ReAct Agent
    agent = ReActAgent(tools=tools, llm=llm, verbose=True)
    
    return agent

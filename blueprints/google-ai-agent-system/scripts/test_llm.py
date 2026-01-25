import os
from dotenv import load_dotenv

load_dotenv()
os.environ["MOCK_AGENTS"] = "False" # Ensure mock is off

from engine.llm_factory import get_llm
try:
    llm = get_llm()
    print(f"Created LLM: {llm}")
    from langchain_core.messages import HumanMessage
    resp = llm.invoke([HumanMessage(content="Hello")])
    print(f"Response: {resp.content}")
except Exception as e:
    import traceback
    traceback.print_exc()

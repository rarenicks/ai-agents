import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = "gemma-3-4b-it"
print(f"Testing model: {model}")

llm = ChatGoogleGenerativeAI(model=model)
try:
    resp = llm.invoke("Hi")
    print(f"Success! Response: {resp.content}")
except Exception as e:
    print(f"Failed: {e}")

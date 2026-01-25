from typing import List, Dict
from duckduckgo_search import DDGS
from langchain_core.tools import tool

def web_search(query: str) -> str:
    """Performs a web search using DuckDuckGo. Use this to find information about current events, specific facts, or updated data."""
    try:
        print(f"Searching for: {query}")
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=5)]
        if not results:
            return "No results found."
        formatted_results = "\n\n".join([f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}" for r in results])
        return formatted_results
    except Exception as e:
        return f"Error performing search: {str(e)}"

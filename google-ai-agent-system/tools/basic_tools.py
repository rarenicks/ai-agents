from langchain_core.tools import tool

def calculate_length(text: str) -> int:
    """Calculates the length of the input text."""
    return len(text)

def get_weather(city: str) -> str:
    """Mock tool to get weather for a city."""
    return f"The weather in {city} is sunny and 25°C (Simulated)."

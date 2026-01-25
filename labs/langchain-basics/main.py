import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# --- Configuration ---
# Set your OpenAI API key as an environment variable.
# It's recommended to set this in your shell/system environment.
# Example for Linux/macOS: export OPENAI_API_KEY='your_api_key_here'
# Example for Windows (CMD): set OPENAI_API_KEY=your_api_key_here
# Example for Windows (PowerShell): $env:OPENAI_API_KEY="your_api_key_here"

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY environment variable not set. "
        "Please set it before running the script."
    )

# Initialize the Large Language Model (LLM)
# We're using 'gpt-4o-mini' for its balance of cost-effectiveness and performance.
# 'temperature' controls the randomness of the output:
#   - 0.0 makes the output very deterministic.
#   - 1.0 makes it highly creative and random.
# We'll use 0.7 for a good balance of creativity and consistency.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --- Define the Prompt Template ---
# This ChatPromptTemplate guides the LLM on how to generate the article.
# It uses a 'system' message to set the persona and a 'user' message with instructions.
# The '{topic}' is a placeholder that will be filled dynamically when the chain is invoked.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced content writer known for creating clear, engaging, and factually accurate articles."),
    ("user", """
        Write a short article (around 200-300 words) about "{topic}".
        The article should cover the following key benefits:
        - Stress reduction
        - Improved focus and concentration
        - Enhanced emotional regulation
        - Better sleep quality

        Ensure the article is well-structured with a clear title and separate paragraphs
        for each specified benefit. The language should be easy for a general audience to understand.
        Provide only the article content, no extra commentary.
    """)
])

# --- Define the Output Parser ---
# The StrOutputParser simply takes the LLM's output (which is a message object)
# and extracts its content as a plain string.
output_parser = StrOutputParser()

# --- Create the LangChain Chain ---
# This is where we link our components together using LangChain Expression Language (LCEL).
# The '|' operator (pipe) means the output of the left component becomes the input of the right.
# So, the input goes to 'prompt', its output goes to 'llm', and the LLM's output goes to 'output_parser'.
content_writer_chain: Runnable = prompt | llm | output_parser

# --- Run the Chain ---
if __name__ == "__main__":
    print("## Starting LangChain Content Writer...\n")

    # Define the specific topic for our article.
    article_topic = "The Benefits of Daily Meditation"

    # Invoke the chain with the defined topic.
    # The 'invoke' method executes the entire chain with the given input dictionary.
    result = content_writer_chain.invoke({"topic": article_topic})

    print("\n## Content Generation Completed!\n")
    print(f"### Here's the article on '{article_topic}':\n")
    print(result)
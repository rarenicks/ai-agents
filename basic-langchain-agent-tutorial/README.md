# Basic Content Writer Agent with LangChain

This repository demonstrates how to build a basic AI agent for content generation using the **LangChain framework** directly. Unlike `CrewAI`, which orchestrates multiple agents and tasks, this example focuses on using core LangChain components: **Large Language Models (LLMs)**, **Prompt Templates**, and **Chains** to achieve a specific writing task.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [main.py Explained](#mainpy-explained)
- [Expected Output](#expected-output)
- [Next Steps](#next-steps)

---

## Overview

This project features a simple content writer setup using LangChain. It will:

1.  Take a predefined **topic**.
2.  Use a **prompt template** to instruct an **LLM** on how to write an article about that topic.
3.  Execute this process as a **LangChain expression language (LCEL) chain**.

The goal is to generate a concise, informative article on "The Benefits of Daily Meditation."

---

## Prerequisites

Before you start, make sure you have:

* **Python 3.10+** installed.
* An **OpenAI API Key**. You can obtain one from the [OpenAI platform](https://platform.openai.com/account/api-keys).

---

## Project Structure

The project has a minimal structure:


├── main.py
└── README.md


* `main.py`: Contains all the Python code for defining and running the LangChain content writer.
* `README.md`: This documentation file.

---

## How to Run

Follow these steps to get the content writer running:

1.  **Create `main.py`**:
    Create a file named `main.py` in your project directory and paste the code from the [`main.py` Explained](#mainpy-explained) section into it.

2.  **Install Dependencies**:
    It's highly recommended to use a Python virtual environment.

    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

    Then, install the necessary libraries:

    ```bash
    pip install langchain-openai langchain
    ```

3.  **Set Your OpenAI API Key**:
    You must set your OpenAI API key as an **environment variable** before running the script. **Replace `YOUR_OPENAI_API_KEY_HERE` with your actual key.**

    * **macOS/Linux**:
        ```bash
        export OPENAI_API_KEY='YOUR_OPENAI_API_KEY_HERE'
        ```
    * **Windows (Command Prompt)**:
        ```cmd
        set OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
        ```
    * **Windows (PowerShell)**:
        ```powershell
        $env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
        ```

4.  **Execute the Script**:
    Run the `main.py` file from your terminal:

    ```bash
    python main.py
    ```

---

## `main.py` Explained

The `main.py` file sets up a direct LangChain process to generate an article.

```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# --- Configuration ---
# Set your OpenAI API key as an environment variable.
# It's recommended to set this in your shell/system environment.
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it before running.")

# Initialize the Large Language Model (LLM)
# Using gpt-4o-mini for cost-effectiveness and speed.
# temperature controls randomness (0.0 for deterministic, 1.0 for creative).
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --- Define the Prompt Template ---
# This template guides the LLM on how to write the article.
# It includes placeholders for dynamic content like 'topic'.
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
# This parser simply takes the LLM's output and ensures it's a string.
# Useful for simple cases, and essential for more complex parsing (e.g., JSON).
output_parser = StrOutputParser()

# --- Create the LangChain Chain ---
# A chain combines components in a sequence: Prompt -> LLM -> Output Parser.
# The '|' operator (pipe) is part of LangChain Expression Language (LCEL)
# which allows easy chaining of Runnables.
content_writer_chain: Runnable = prompt | llm | output_parser

# --- Run the Chain ---
if __name__ == "__main__":
    print("## Starting LangChain Content Writer...\n")

    # Define the topic for the article
    article_topic = "The Benefits of Daily Meditation"

    # Invoke the chain with the specific topic
    # The 'invoke' method runs the entire chain with the given input.
    result = content_writer_chain.invoke({"topic": article_topic})

    print("\n## Content Generation Completed!\n")
    print(f"### Article on '{article_topic}':\n")
    print(result)

```

# Expected Output
When you run main.py, you'll see console output indicating the start and completion of the content generation process. Finally, the complete article generated by the LangChain setup will be printed to your terminal. Since there's no verbose output like in CrewAI by default, the process will appear more streamlined.


# Next Steps
- Customize the Task: Change the article_topic variable in main.py to generate content on a different subject.
- Refine the Prompt: Experiment with the prompt template to change the article's tone, length, or required sections.
- Add More Complexity: Explore LangChain's features to add more advanced functionality:
  - Tools: Integrate tools for web searching or data retrieval before writing.
  - Memory: Give the "agent" memory to recall past interactions.
  - Routing: Create a system that routes different prompts to different LLMs or chains.
- Explore Other Models: Try different ChatOpenAI models (e.g., gpt-3.5-turbo, gpt-4) or even models from other providers supported by LangChain.
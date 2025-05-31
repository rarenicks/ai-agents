# Basic Content Writer Agent with CrewAI

This repository contains a simple AI agent built using the `CrewAI` framework. Its purpose is to demonstrate how to set up a basic agent to generate concise and informative articles on a specific topic.

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

This project features a single AI agent, the **"Content Writer"**. This agent is tasked with writing a short article about "The Benefits of Daily Meditation."

The key components of this `CrewAI` setup are:

* **Agent**: An autonomous AI entity with a defined **role**, **goal**, and **backstory**.
* **Task**: A specific objective for an agent, including a detailed **description** and **expected\_output**.
* **Crew**: The orchestrator that brings agents and tasks together to execute a workflow.

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


* `main.py`: Contains all the Python code for defining and running the `CrewAI` agent.
* `README.md`: This documentation file.

---

## How to Run

Follow these steps to get the content writer agent running:

1.  **Create `main.py`**:
    Create a file named `main.py` in your project directory and paste the code provided in the `main.py`. 

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
    pip install crewai langchain-openai
    ```

3.  **Set Your OpenAI API Key**:
    You must set your OpenAI API key as an **environment variable** before running the script. Replace `YOUR_OPENAI_API_KEY_HERE` with your actual key.

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

The `main.py` file orchestrates the content creation process.

```python
import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from textwrap import dedent

# Configuration: Set your OpenAI API key and initialize the LLM
# The LLM (Large Language Model) used is 'gpt-4o-mini' for efficiency.
# 'temperature=0.7' balances creativity and consistency in the output.
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it before running.")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Agent Definition: The Content Writer
# This agent has a specific role, a clear goal, and a backstory to guide its behavior.
# 'verbose=True' allows you to see the agent's internal thinking process during execution.
content_writer = Agent(
    role='Content Writer',
    goal='Write a concise and informative article about a given topic.',
    backstory=dedent("""
        You are an experienced content writer known for your ability to
        create clear, engaging, and factually accurate articles.
    """),
    verbose=True,
    allow_delegation=False, # Set to False as there's only one agent here
    llm=llm
)

# Task Definition: The writing assignment
# This defines exactly what needs to be done and what the expected output should look like.
# The task is assigned to the 'content_writer' agent.
writing_task = Task(
    description=dedent("""
        Write a short article (200-300 words) about "The Benefits of Daily Meditation".
        The article should cover stress reduction, improved focus, emotional regulation, and better sleep.
        Include a clear title and separate paragraphs for each specified benefit.
    """),
    expected_output=dedent("""
        A well-structured article (200-300 words) with a title, an introduction,
        separate paragraphs for each benefit (stress reduction, focus, emotional regulation, sleep),
        and a concluding paragraph.
    """),
    agent=content_writer,
)

# Crew Assembly: Brings the agent and task together to form an operational unit.
# 'Process.sequential' means tasks run in the order they are defined.
# 'verbose=True' displays the overall crew's progress and task status.
my_crew = Crew(
    agents=[content_writer],
    tasks=[writing_task],
    process=Process.sequential,
    verbose=True
)

# Run the Crew: This starts the entire execution process.
if __name__ == "__main__":
    print("## Kicking off the Content Creation Crew...\n")
    # kickoff() initiates the crew's work and returns the final output of the last task.
    result = my_crew.kickoff()
    print("\n## Crew Work Completed!\n")
    print("### Here is the article generated by the Content Writer:\n")
    print(result)

```

## Expected Output
When you run main.py, you'll see a detailed log in your terminal. This output shows the Content Writer agent's thinking process, its actions, and the overall task execution status (thanks to verbose=True). Finally, the complete article generated by the agent will be printed to the console.


## Next Steps
- Customize the Task: Change the description and expected_output of the writing_task to generate articles on different topics or with different requirements.
- Adjust Creativity: Experiment with the temperature parameter of the ChatOpenAI model (0.0 for more factual/deterministic output, 1.0 for more creative/varied output).
- Expand with More Agents: Consider how you might add another agent, like a "Research Analyst," to gather information before the "Content Writer" starts writing. This would involve adding a tool (e.g., a web search tool) to the research agent.
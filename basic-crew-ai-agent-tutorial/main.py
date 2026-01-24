import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from textwrap import dedent

# --- Configuration ---
# Ensure your OpenAI API key is set as an environment variable
# If not, uncomment the line below and replace with your key
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Initialize the Large Language Model (LLM)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --- Define Agents ---
content_writer = Agent(
    role='Content Writer',
    goal='Write a concise and informative article about a given topic.',
    backstory=dedent("""
        You are an experienced content writer known for your ability to
        create clear, engaging, and factually accurate articles. You are
        diligent and ensure your writing is easy to understand.
    """),
    verbose=True, # Set to True to see the agent's thought process
    allow_delegation=False,
    llm=llm
)

# --- Define Tasks ---
writing_task = Task(
    description=dedent("""
        Write a short article (around 200-300 words) about "The Benefits of Daily Meditation".
        The article should cover:
        - Stress reduction
        - Improved focus
        - Emotional regulation
        - Better sleep
        Format the article with a clear title and paragraphs.
    """),
    expected_output=dedent("""
        A well-structured article of 200-300 words, including a title and paragraphs,
        detailing the benefits of daily meditation, specifically addressing
        stress reduction, improved focus, emotional regulation, and better sleep.
    """),
    agent=content_writer,
)

# --- Create the Crew ---
my_crew = Crew(
    agents=[content_writer],
    tasks=[writing_task],
    process=Process.sequential,
    verbose=True # Set to True to see the overall crew's execution
)

# --- Run the Crew ---
if __name__ == "__main__":
    print("## Kicking off the Content Creation Crew...\n")
    result = my_crew.kickoff()
    print("\n## Crew Work Completed!\n")
    print("### Here is the article:\n")
    print(result)
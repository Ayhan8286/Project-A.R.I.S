import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

# Verify API key is set
if "GROQ_API_KEY" not in os.environ:
    raise ValueError("Please set the GROQ_API_KEY environment variable.")

# Initialize the Groq LLM
llm = ChatGroq(
    temperature=0,
    model_name="groq/llama-3.3-70b-versatile",
    api_key=os.environ["GROQ_API_KEY"]
)

# Define an Agent
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define a Task
task1 = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI agents
    in 2024. Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="""A detailed report summarizing major AI agent trends,
    highlighting key technologies and their implications for the future.""",
    agent=researcher
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher],
    tasks=[task1],
    verbose=True,
    process=Process.sequential
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)

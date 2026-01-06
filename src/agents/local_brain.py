import os
from crewai import Agent, Task, Crew, Process

# Configure environment variables for Ollama compatibility
# The "Imposter" strategy: Point OpenAI API base to local Ollama instance
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3'  # Ensure you have pulled this model in Ollama
os.environ["OPENAI_API_KEY"] = 'NA' # API key is not required for local Ollama

# Define a Local Agent
local_researcher = Agent(
    role='Local Knowledge Expert',
    goal='Provide insights using locally hosted intelligence',
    backstory="""You are an AI assistant running entirely on local hardware.
    You prioritize privacy and speed, relying on your internal knowledge base.""",
    verbose=True,
    allow_delegation=False
)

# Define a Task
local_task = Task(
    description="""Explain the benefits of running Large Language Models locally
    versus in the cloud. Focus on data privacy, latency, and cost.""",
    expected_output="""A concise comparison highlighting the advantages of
    local LLM deployment.""",
    agent=local_researcher
)

# Instantiate the Crew
local_crew = Crew(
    agents=[local_researcher],
    tasks=[local_task],
    verbose=True,
    process=Process.sequential
)

# Kickoff
print("Starting Local Brain...")
result = local_crew.kickoff()
print("######################")
print(result)

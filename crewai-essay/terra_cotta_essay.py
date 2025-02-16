import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define Agents
researcher = Agent(
    role='Historical Researcher',
    goal='Investigate and validate historical facts about the Terracotta Warriors',
    backstory="""A meticulous historian specializing in ancient Chinese archaeology 
    and Qin Dynasty artifacts. You have access to academic databases and historical records.""",
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='Professional Writer',
    goal='Craft a compelling, well-structured essay about the Terracotta Warriors',
    backstory="""An award-winning historical writer with expertise in making 
    archaeological discoveries accessible to general audiences.""",
    verbose=True,
    allow_delegation=False
)

# Define Tasks
research_task = Task(
    description="""Conduct thorough research on:
    1. Discovery history (1974)
    2. Emperor Qin Shi Huang's mausoleum
    3. Construction techniques
    4. Cultural significance
    5. Current preservation efforts
    Include verified statistics and academic sources""",
    expected_output="Bullet-point research notes with key facts and sources",
    agent=researcher
)

writing_task = Task(
    description="""Using the research, write a 1500-word essay with:
    1. Introduction hook
    2. Historical context
    3. Archaeological significance
    4. Cultural impact
    5. Modern preservation challenges
    Maintain academic rigor while being engaging""",
    expected_output="Polished essay in Markdown format with section headers",
    agent=writer
)

# Assemble Crew
essay_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)

# Previous code remains the same until crew execution...

# Execute Crew
result = essay_crew.kickoff()

# Save Output (simplified)
with open("terracotta_warriors_essay.md", "w", encoding="utf-8") as f:
    f.write(result)  # Direct string write

print("Essay generated successfully!")
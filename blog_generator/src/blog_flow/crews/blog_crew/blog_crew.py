from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class BlogCrew:
    """Blog Crew for writing about Pakistan's history"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def history_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["history_writer"],
        )

    @task
    def write_blog(self) -> Task:
        return Task(
            config=self.tasks_config["write_blog"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Blog Writing Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        ) 
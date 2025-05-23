"""
Example agent using CrewAI.
"""
from crewai import Agent
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_community.tools import DuckDuckGoSearchRun

class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(..., description="Search query for DuckDuckGo.")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Searches the web using DuckDuckGo."
    args_schema: Type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)

def create_researcher_agent() -> Agent:
    """Create a researcher agent."""
    search_tool = DuckDuckGoSearchTool()
    return Agent(
        role='Research Analyst',
        goal='Conduct thorough research on given topics',
        backstory="""You are an expert research analyst with years of experience
        in gathering and analyzing information from various sources.""",
        tools=[search_tool],
        verbose=True,
        allow_delegation=False
    )

def create_writer_agent() -> Agent:
    """Create a writer agent."""
    return Agent(
        role='Content Writer',
        goal='Create engaging and informative content',
        backstory="""You are a skilled content writer with expertise in
        creating clear and engaging content from research materials.""",
        verbose=True,
        allow_delegation=False
    ) 
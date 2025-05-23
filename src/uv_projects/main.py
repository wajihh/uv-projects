"""
Main entry point for the UV Projects application.
"""
import logging
from typing import Any
from crewai import Crew, Process
from dotenv import load_dotenv

from uv_projects.agents.example_agent import create_researcher_agent, create_writer_agent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Run the main application."""
    try:
        # Load environment variables
        load_dotenv()
        logger.info("Environment variables loaded successfully")

        # Create agents
        researcher = create_researcher_agent()
        writer = create_writer_agent()
        logger.info("Agents created successfully")

        # Create a crew
        crew = Crew(
            agents=[researcher, writer],
            tasks=[
                {
                    "description": "Research the latest developments in AI",
                    "agent": researcher,
                    "expected_output": "A list of key findings and recent advancements in AI."
                },
                {
                    "description": "Write a summary of the research findings",
                    "agent": writer,
                    "expected_output": "A clear, concise summary article based on the research findings."
                }
            ],
            process=Process.sequential,
            verbose=True
        )
        logger.info("Crew created successfully")

        # Run the crew
        result = crew.kickoff()
        logger.info("Crew execution completed")
        
        print("\nFinal Result:")
        print(result)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main() 
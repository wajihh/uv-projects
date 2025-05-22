#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from blog_flow.crews.blog_crew.blog_crew import BlogCrew


class BlogState(BaseModel):
    section_count: int = 1
    blog: str = ""


class BlogFlow(Flow[BlogState]):

    @start()
    def generate_section_count(self):
        print("Generating section count")
        self.state.section_count = randint(3, 6)

    @listen(generate_section_count)
    def generate_blog(self):
        print("Generating blog")
        result = (
            BlogCrew()
            .crew()
            .kickoff(inputs={"section_count": self.state.section_count})
        )

        print("Blog generated", result.raw)
        self.state.blog = result.raw

    @listen(generate_blog)
    def save_blog(self):
        print("Saving blog")
        with open("pakistan_history_blog.txt", "w") as f:
            f.write(self.state.blog)


def kickoff():
    blog_flow = BlogFlow()
    blog_flow.kickoff()


def plot():
    blog_flow = BlogFlow()
    blog_flow.plot()


if __name__ == "__main__":
    kickoff() 
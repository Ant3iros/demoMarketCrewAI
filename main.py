import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks


from langchain.tools import DuckDuckGoSearchRun

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py
class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        newsSearcher = agents.newsSearcher()
        newsWriter = agents.newsWriter()
        newsTranslator = agents.newsTranslator()

        # Custom tasks include agent name and variables as input
        news_search_task = tasks.news_search_task(
            newsSearcher,
            self.var1
        )

        writer_task = tasks.writer_task(
            newsWriter,
            news_search_task
        )

        translator_task = tasks.translater_task(
            newsTranslator,
            writer_task
        )

        # Define your custom crew here
        crew = Crew(
            agents=[newsSearcher, newsWriter, newsTranslator],
            tasks=[news_search_task, writer_task, translator_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    #subject = input(dedent("""Enter variable 1: """))
    subject = """Golem.ai company"""
    custom_crew = CustomCrew(subject)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
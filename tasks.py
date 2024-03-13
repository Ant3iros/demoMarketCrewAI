from crewai import Task
from tools.searchNewsDB import *


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def news_search_task(self, agent, var1):
        return Task(
            description=f'Search for {var1} and create key points for each news, marketing oriented ( marketing mix 4P product, place, price, promotion)',
            agent=agent,
            expected_output="bullet points",
            tools=[SearchNewsDB().news]
        )

    def writer_task(self, agent, newsSearchTask):
        return Task(
            description="""
            Go step by step.
            Step 1: Identify all the topics received.
            Step 2: Use the Get News Tool to verify the each topic by going through one by one.
            Step 3: Use the SearchTool DuckDuck to search for information on each topic one by one and market details about it. 
            Step 4: Go through every topic and write an in-depth market summary of the information retrieved.
            Don't skip any topic.
            """,
            agent=agent,
            context=[newsSearchTask],
            expected_output="market report and quick answer about my question",
            tools=[GetNews().news, searchTool.searchTool()]
        )

    def translater_task(self, agent, writeOfWriter):
        return Task(
            description="""
            translate in french
            """,
            agent=agent,
            context=[writeOfWriter],
            expected_output="translation for report in the company"
        )
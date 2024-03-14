from crewai import Agent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.searchNewsDB import *


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.OpenAIGPT4T = ChatOpenAI(model_name="gpt-4-turbo-preview", temperature=0.7)
        self.Ollama = Ollama(model="mistral")

    def newsSearcher(self):
        return Agent(
            role='News Seacher',
            goal='Generate key points for each news article from the latest news',
            backstory='Expert in analysing and generating key points from news content for quick updates.',
            tools=[SearchNewsDB().news],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT4T
        )

    def newsWriter(self):
        return Agent(
            role='Writer',
            goal="""Identify all the topics received. 
            Use the Get News Tool to verify the each topic to search. 
            Use the Search tool for detailed exploration of each topic in marketing view like product, concurrent, price, place, promotion.
            Summarise the retrieved information in depth for every topic. 
            You have to be succinct""",
            backstory='Expert in crafting engaging narratives from complex information.',
            tools=[GetNews().news, searchTool.searchTool()],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT4T
        )

    def newsTranslator(self):
        return Agent(
            role='Translator',
            goal='Translate in french.',
            backstory='Translator in french, use a professionnal french for reports',
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama
        )

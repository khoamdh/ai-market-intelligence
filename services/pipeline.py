from ai.agents import MarketAgent
from core.tools import TOOLS

def run_system(question, llm):
    agent = MarketAgent(llm=llm, tools=TOOLS)
    return agent.run(question)
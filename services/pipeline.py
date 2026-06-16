from ai.agents import MarketAgent

def run_system(question, llm, tools):
    agent = MarketAgent(llm, tools)
    return agent.run(question)
class MarketAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def run(self, question):
        # 1. simple routing logic (manual agent first)
        if "correlation" in question:
            corr = self.tools["get_correlation"]()

            context = f"""
            Correlation BTC vs S&P500: {corr}
            Question: {question}
            """

        elif "price" in question:
            btc = self.tools["get_btc"]()
            context = btc.tail(10).to_string()

        else:
            context = question

        # 2. reasoning step
        return self.llm(context)
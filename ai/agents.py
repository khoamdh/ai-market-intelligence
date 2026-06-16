class MarketAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def run(self, question):

        q = question.lower()

        # TOOL EXECUTION
        btc = self.tools["get_btc"]()
        sp500 = self.tools["get_sp500"]()

        # CORRELATION CASE
        if "correlation" in q:

            corr = self.tools["get_correlation"]()

            corr_value = corr.get("correlation")
            samples = corr.get("samples", 0)
            note = corr.get("message", "")

            context = f"""
You are a financial analyst.

BTC vs S&P500 correlation: {corr_value}
Samples: {samples}
{f"Note: {note}" if note else ""}

Explain this result.
"""

            analysis = self.llm(context)

            return {
                "data": None,
                "analysis": analysis
            }

        # PRICE / TREND CASE
        context = f"""
You are a financial analyst.

BTC data:
{btc.tail(30).to_string()}

S&P500 data:
{sp500.tail(30).to_string()}

Question:
{question}
"""

        analysis = self.llm(context)

        return {
            "data": btc,   # or sp500 or merged if you want later
            "analysis": analysis
        }
class MarketAgent:
    def __init__(self, llm, tools):
        """
        llm: function that takes a prompt and returns response
        tools: dictionary of callable tool functions
        """
        self.llm = llm
        self.tools = tools

    def run(self, question: str):
        """
        Tool-augmented single-agent workflow:
        1. Understand intent (rule-based lightweight routing)
        2. Call appropriate tools
        3. Build structured context
        4. Send to LLM for reasoning
        """

        context = ""

        # ----------------------------
        # 1. CORRELATION ANALYSIS
        # ----------------------------
        if "correlation" in question.lower():
            corr = self.tools["get_correlation"]()

            context = f"""
You are a financial analyst.

Task: Analyze relationship between Bitcoin and S&P 500.

Data:
- BTC vs S&P500 correlation: {corr}

User question:
{question}

Instructions:
- Explain what this correlation means
- Interpret market relationship (divergence vs coupling)
- Keep response concise and structured
"""

        # ----------------------------
        # 2. PRICE / MARKET TREND ANALYSIS
        # ----------------------------
        elif "price" in question.lower() or "trend" in question.lower():

            btc = self.tools["get_btc"](period="5y")  # IMPORTANT FIX: no tail(10)

            context = f"""
You are a financial analyst.

Task: Analyze Bitcoin price trends.

Dataset summary:
- Time range: {btc.index.min()} → {btc.index.max()}
- Latest prices:
{btc['Close'].tail(30).to_string()}

User question:
{question}

Instructions:
- Identify short-term vs long-term trend
- Highlight volatility patterns
- Avoid assuming missing data
"""

        # ----------------------------
        # 3. GENERAL MARKET QUESTION
        # ----------------------------
        else:
            sp500 = self.tools["get_sp500"](period="5y")
            btc = self.tools["get_btc"](period="5y")

            context = f"""
You are a financial analyst.

Task: Provide general market insights.

Data summary:
- S&P500 range: {sp500.index.min()} → {sp500.index.max()}
- BTC range: {btc.index.min()} → {btc.index.max()}

User question:
{question}

Instructions:
- Compare macro trends if relevant
- Be structured and analytical
"""

        # ----------------------------
        # 4. LLM REASONING STEP
        # ----------------------------
        response = self.llm(context)

        return response
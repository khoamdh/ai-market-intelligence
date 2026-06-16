import os

import streamlit as st

from ai.llm import ask_llm
from services.pipeline import run_system
from ui.dashboard import render_dashboard

st.set_page_config(page_title="AI Market Intelligence", layout="wide")
st.title("AI Market Intelligence")

if not os.getenv("OPENAI_API_KEY"):
    st.info("Add `OPENAI_API_KEY` to a `.env` file in the project root to enable AI analysis.")

question = st.text_input(
    "Ask a market question",
    placeholder="e.g. What is the BTC vs S&P 500 correlation?",
)

if question:
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not configured.")
    else:
        with st.spinner("Analyzing market data..."):
            result = run_system(question, ask_llm)

        render_dashboard(result["data"], result["analysis"])

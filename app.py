import streamlit as st
from data_loader import fetch_data
from analytics import compute_features
from llm import ask_llm

st.title("AI Market Intelligence Assistant")

question = st.text_input("Ask a question about S&P 500 and Bitcoin")

if question:
    sp500 = fetch_data("^GSPC")
    btc = fetch_data("BTC-USD")

    df = compute_features(sp500, btc)

    latest = df.tail(30)

    context = f"""
You are a financial analyst.

Question:
{question}

Data (last 30 rows):
{latest.to_string(index=False)}

Focus on:
- correlation
- volatility
- risk-on vs risk-off behavior
"""

    answer = ask_llm(context)

    st.write(answer)
import streamlit as st
from services.pipeline import run_system
from ai.llm import ask_llm
from core.tools import get_correlation, get_btc

tools = {
    "get_correlation": get_correlation,
    "get_btc": get_btc
}

st.title("AI Market System")

question = st.text_input("Ask a question")

if question:
    answer = run_system(question, ask_llm, tools)
    st.write(answer)
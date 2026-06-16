import streamlit as st

def render_dashboard(data, analysis):
    st.title("AI Market Intelligence")

    st.subheader("Market Data")
    st.dataframe(data.tail())

    st.subheader("AI Analysis")
    st.write(analysis)
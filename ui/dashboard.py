import streamlit as st


def render_dashboard(data, analysis):
    st.markdown("---")

    # MARKET DATA SECTION
    st.subheader("Market Data (Latest Snapshot)")

    if data is not None:
        st.dataframe(data.tail(30), use_container_width=True)
    else:
        st.warning("No market data available")

    # AI ANALYSIS SECTION
    st.subheader("AI Analysis")

    if analysis:
        st.write(analysis)
    else:
        st.warning("No analysis generated")

    st.markdown("---")
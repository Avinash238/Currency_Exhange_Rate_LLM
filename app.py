import streamlit as st
from currency_correlation_analysis import analyze_correlation

st.title("Currency Correlation Analysis App")

currencies = st.text_area("Enter Currencies (comma-separated):", "USD, EUR, JPY, GBP")


if st.button("Analyze Currency Correlation"):
    st.write("### Analyzing...")

    # Call the analysis function
    insights = analyze_correlation(currencies)

    st.write("### Analysis Results:")
    st.write(insights)

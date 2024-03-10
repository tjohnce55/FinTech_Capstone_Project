"""
This page will allow the user to enter a stock ticker and obtain useful fundamental data about that company.

When an error occurs, or exception, Python will stop and generate an error message.
We will handle these exceptions using the try and except statements.
If the user enters an invalid ticker they will be asked to reenter a valid ticker rather than Python giving them an error message.
"""

# Import the required libraries and dependencies.
import streamlit as st
import yfinance as yf

# Display a title for the the fundamental analysis page.
st.header("📝 Fundamental Analysis Tool")

# Display a subheader that explains the tool along with a disclaimer.
st.write("Enter a ticker below. The tool will obtain and display fundamental data for the company of your choice.")
st.write("DISCLAIMER: Please remember that past performance may not be indicative of future results. The data that appears does not represent financial advice.")

st.divider()

# Create a text input for the user to enter a stock ticker.
ticker = st.text_input("⬇️ Enter a Stock Ticker")

# Only have the simulation run once the user clicks the "Submit" button.
if st.button("Submit"):
    # Create a variable that downloads data from yfinance using the ticker input.
    stock_data = yf.Ticker(ticker)
    
    fundamentals = stock_data.info
    
    # Display the company's name as the header for the fundamentals that appear.
    st.header(fundamentals["shortName"])

    # Display the metrics in three columns to fit the screen better on Streamlit.
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Sector", fundamentals["sector"])
    with col2:
        st.metric("Industry", fundamentals["industry"])
    st.metric("Website", fundamentals["website"])
        
    business_summary, metrics, income_statement, balance_sheet, cash_flow, inst_holders = st.tabs(["Business Summary", "Metrics", "Income Statement", "Balance Sheet", "Cash Flow", "Institutional Holders"])
    
    with business_summary:
        st.write(fundamentals["longBusinessSummary"])
        
    with metrics:
        column1, column2 = st.columns(2)
        with column1:
            st.metric("Market Cap", fundamentals["marketCap"])
            st.metric("Dividend Yield", fundamentals["dividendYield"])
            st.metric("Beta", fundamentals["beta"])
            st.metric("Trailing PE", fundamentals["trailingPE"])
            st.metric("Price-To-Book", fundamentals["priceToBook"])
            st.metric("Yahoo Finance Recommendation", fundamentals["recommendationKey"])
        with column2:
            st.metric("Quick Ratio", fundamentals["quickRatio"])
            st.metric("Current Ratio", fundamentals["currentRatio"])
            st.metric("Deb-To-Equity", fundamentals["debtToEquity"])
            st.metric("Return on Equity", fundamentals["returnOnEquity"])
            st.metric("Target Mean Price", fundamentals["targetMeanPrice"]) 
        
    with income_statement:
        st.dataframe(stock_data.income_stmt)
        
    with balance_sheet:
        st.dataframe(stock_data.balance_sheet)
        
    with cash_flow:
        st.dataframe(stock_data.cashflow)
        
    with inst_holders:
        st.dataframe(stock_data.institutional_holders)
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
    # Create a catch-all (using try and except statements) in case the user enters an invalid stock ticker.
    try:
        # Create a variable that downloads data from yfinance using the ticker input.
        # Create a variable for just the fundamental data obtain from yfinance.
        stock_data = yf.Ticker(ticker)
        fundamentals = stock_data.info

        # Display the company's name as the header for the fundamentals that appear.
        st.header(fundamentals["shortName"])

        # Display the metrics in two columns to fit the screen better on Streamlit.
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sector", fundamentals["sector"])
        with col2:
            st.metric("Industry", fundamentals["industry"])
        st.metric("Website", fundamentals["website"])

        # Create tabs that will obtain different data and tables.
        business_summary, metrics, income_statement, balance_sheet, cash_flow, inst_holders = st.tabs(["Business Summary", "Metrics", "Income Statement", "Balance Sheet", "Cash Flow", "Institutional Holders"])

        # Display the business summary within the "Business Summary" tab.
        with business_summary:
            st.write(fundamentals["longBusinessSummary"])

        # Display various metrics within the "Metrics" tab.
        # Create two columns to organize the metrics better.
        # Round certain metrics to two decimal places and also write the ratio's formula.
        with metrics:
            column1, column2 = st.columns(2)
            with column1:
                market_cap = "{:,}".format(fundamentals["marketCap"])
                st.metric("Market Cap:", market_cap)
                dividend = round(fundamentals["dividendYield"] * 100, 2)
                st.metric("Dividend Yield: (%)", dividend)
                st.metric("Beta:", fundamentals["beta"])
                trailing_pe = round(fundamentals["trailingPE"], 2)
                st.metric("Trailing PE: (Share Price / Recent EPS)", trailing_pe)
                price_to_book = round(fundamentals["priceToBook"], 2)
                st.metric("Price-To-Book", price_to_book)
                st.metric("Yahoo Finance Recommendation:", fundamentals["recommendationKey"])
            with column2:
                quick_ratio = round(fundamentals["quickRatio"], 2)
                st.metric("Quick Ratio: (Liquid Assets / Current Liabilities)", quick_ratio)
                current_ratio = round(fundamentals["currentRatio"], 2)
                st.metric("Current Ratio: (Current Assets / Current Liabilities)", current_ratio)
                debt_to_equity = round(fundamentals["debtToEquity"], 2)
                st.metric("Debt-To-Equity: (Total Debt / Total Shareholder Equity)", debt_to_equity)
                return_on_equity = round(fundamentals["returnOnEquity"], 2)
                st.metric("Return on Equity: (Net Income / Avg Shareholder Equity)", return_on_equity)
                st.metric("Target Mean Price:", fundamentals["targetMeanPrice"]) 

        # Display the annual income statements for the last four years within the "Income Statement" tab.
        with income_statement:
            st.dataframe(stock_data.income_stmt)

        # Display the annual balance sheets for the last four years within the "Balance Sheet" tab.
        with balance_sheet:
            st.dataframe(stock_data.balance_sheet)

        # Display the annual cash flow statements for the last four years within the "Cash Flow" tab.
        with cash_flow:
            st.dataframe(stock_data.cashflow)

        # Display the current institutional holders within the "Institutional Holders" tab.
        with inst_holders:
            st.dataframe(stock_data.institutional_holders)
        
    # Display a warning message that appears when the user enters an invalid stock ticker.
    except:
        st.warning("Oops, please enter a valid stock ticker!")
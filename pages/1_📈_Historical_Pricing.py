# Import the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import yfinance as yf
import plotly.express as px

# Create a title for the the pricing data
st.subheader("Stock Pricing Tool")

# Create a text input for the stock ticker
ticker = st.text_input("Enter a Stock Ticker")

# Create date inputs for the start date and end date for price history
column1, column2 = st.columns(2)
with column1:
    start_date = st.date_input("Select Start Date")
with column2:
    end_date = st.date_input("Select End Date")


# Create a variable that downloads price data from yfinance using the ticker, start_date, and end_date inputs
# Have the price data appear as a line plot
# Only have the line plot appear once they click the "Submit" button
if st.button("Submit"):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    high = round(max(stock_data["High"]), 2)
    low = round(min(stock_data["Low"]), 2)
    price_difference = high - low
    percentage_difference = round((price_difference / low) * 100, 2)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Highest Price", f"${high}")
    with col2:
        st.metric("Lowest Price", f"${low}")
    with col3:
        st.metric("Price Difference (% Change)", f"${price_difference}", f"{percentage_difference}%")
    price_plot = px.line(stock_data, x=stock_data.index, y=stock_data["Adj Close"], title=ticker)
    st.plotly_chart(price_plot)
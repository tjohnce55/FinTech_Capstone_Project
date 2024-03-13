"""
This page will allow the user to enter a stock ticker and a date range of their choosing, and view the price movement of that stock over that time period.
They will also be able to see the highest price, lowest price, and price difference and percent change over that time period.

When an error occurs, or exception, Python will stop and generate an error message.
We will handle these exceptions using the try and except statements.
If the user enters an invalid ticker they will be asked to reenter a valid ticker rather than Python giving them an error message.
"""

# Import the required libraries.
import streamlit as st
import yfinance as yf
import plotly.express as px

# Display a title for the the historical pricing tool.
st.header("📈 Historical Pricing Tool")

# Display a subheader that explains the tool.
st.write("Enter a stock ticker and a date range below. The tool will display the price movement of that stock over the selected time period, along with the highest price, lowest price, and price change.")

# Create a text input for the stock ticker.
ticker = st.text_input("⬇️ Enter a Stock Ticker")

# Create date inputs for the start date and end date.
# Display the date inputs in two columns to fit the screen better on Streamlit.
column1, column2 = st.columns(2)
with column1:
    start_date = st.date_input("Select Start Date")
with column2:
    end_date = st.date_input("Select End Date")

# Only have the pricing data appear once the user clicks the "Submit" button.
if st.button("Submit"):
    # Create a catch-all (using try and except statements) in case the user enters an invalid stock ticker.
    try:
        # Create a variable that downloads price data from yfinance using the ticker, start_date, and end_date inputs.
        stock_data = yf.download(ticker, start_date, end_date)
        
        # Create variables for the high, low, price difference, and percent change. As well as the start and end date prices.
        high = round(max(stock_data["High"]), 2)
        low = round(min(stock_data["Low"]), 2)
        end_date_price = stock_data.iloc[-1]["Close"]
        start_date_price = stock_data.iloc[0]["Close"]
        price_difference = round(end_date_price - start_date_price, 2)
        percentage_difference = round((price_difference / start_date_price) * 100, 2)
        
        # Display the metrics in three columns to fit the screen better on Streamlit.
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Highest Price", f"${high}")
        with col2:
            st.metric("Lowest Price", f"${low}")
        with col3:
            st.metric("Price Difference (% Change)", f"${price_difference}", f"{percentage_difference}%")
            
        # Display the historical price data on Streamlit as a line plot.
        price_plot = px.line(stock_data, x=stock_data.index, y=stock_data["Adj Close"], title=ticker)
        st.plotly_chart(price_plot)
        
    # Display a warning message that appears when the user enters an invalid stock ticker.
    except:
        st.warning("Oops, please enter a valid stock ticker!")

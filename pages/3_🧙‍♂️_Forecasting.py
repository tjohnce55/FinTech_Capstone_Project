"""
This page will allow the user to enter a stock ticker and a hypothetical investment amount.
The tool will use the inputs, gather five years of historical data for that stock, and run a Monte Carlo Simulation to forecast.
They will also be able to see the simulated cumulative return and the simulated value of their investment over the next three years.

When an error occurs, or exception, Python will stop and generate an error message.
We will handle these exceptions using the try and except statements.
If the user enters an invalid ticker they will be asked to reenter a valid ticker rather than Python giving them an error message.
"""

# Import the required libraries and dependencies.
import os
import pandas as pd
import matplotlib.pyplot as plt
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
import streamlit as st

# Load .env enviroment variables.
from dotenv import load_dotenv
load_dotenv()

# Set Alpaca API key and secret key.
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2"
)

# Display a title for the the historical pricing page.
st.header("🧙‍♂️ Forecasting Tool")

# Display a subheader that explains the tool along with a disclaimer.
st.write("Enter a stock ticker and a hypothetical investment amount below. The tool will obtain five years of the stock's historical data and run a Monte Carlo Simulation to forecast three years worth of returns.")
st.write("DISCLAIMER: Please remember that past performance may not be indicative of future results. The forecasts that appear do not represent financial advice.")

st.divider()

# Create a text input for the user to enter a stock ticker.
# Change the "ticker" variable to a str so that it can be interpreted by the api.
ticker = st.text_input("⬇️ Enter a Stock Ticker")
ticker = str(ticker)

# Establish the timeframe to be used and the start and end dates for the historical data.
timeframe = "1Day"
end_date = pd.Timestamp("2024-03-06", tz="America/New_York").isoformat()
start_date = pd.Timestamp("2019-01-01", tz="America/New_York").isoformat()

# Create a slider for the user to enter their hypothetical investment amount.
# Change the "investment" variable from a str to an int so that it can be used in a calculation later.
investment = st.slider("Choose an Investment Amount - Between 1,000 & 100,000 USD", min_value = 1000, max_value = 100000, value = 1000, step=1000)
investment = int(investment)

# Only have the simulation run once the user clicks the "Submit" button.
if st.button("Submit"):
    # Create a catch-all (using try and except statements) in case the user enters an invalid stock ticker.
    try:
        # Use get_bars to obtain the historical data for the stock and make it into a DataFrame.
        ticker_df = api.get_bars(
            ticker,
            timeframe,
            start=start_date,
            end=end_date
        ).df

        # Reorganize the DataFrame.
        ticker_df = pd.concat([ticker_df], axis=1, keys=[ticker])

        # Create a variable for the Monte Carlo Simulation.
        simulation = MCSimulation(
            portfolio_data = ticker_df,
            num_simulation = 500,
            num_trading_days = 252*3
        )
        
        # The download takes a few seconds to run so display a message that informs the user.
        st.write("Please wait while we forecast the data.")
        
        # Run the Monte Carlo Simulation.
        simulation.calc_cumulative_return()

        # Compute summary statistics from the simulated returns.
        simulated_returns_data = {
            "mean": list(simulation.simulated_return.mean(axis=1)),
            "median": list(simulation.simulated_return.median(axis=1)),
        }

        # Create a DataFrame with the summary statistics.
        df_simulated_returns = pd.DataFrame(simulated_returns_data)

        # Multiply the investment by the returns to get the progression of the profit/loss in terms of dollars.
        investment_pnl = investment * df_simulated_returns

        # Use the 'plot' function to visually analyze the simulated profit/loss over the next three years.
        # Plot both mean and median forecasted profit/loss.
        # Display the plot on Streamlit.
        investment_return_plot = plt.plot(investment_pnl[['mean', 'median']])
        plt.legend(['Mean', 'Median'])
        plt.ylabel("Value of Investment (USD)")
        plt.xlabel("Number of Trading Days")
        plt.title("Simulated Investment Return Over the Next Three Years")
        plt.xlim(left=0)
        plt.ylim(bottom=investment/2)
        plt.show()
        st.pyplot(plt)

        # Create a table that summarizes the cumulative returns.
        tbl = simulation.summarize_cumulative_return()

        # Calculate the lower and upper confidence intervals using the user's investment amount.
        ci_lower = round(tbl[8]*investment,2)
        ci_upper = round(tbl[9]*investment,2)

        # Multiply the table values by the investment amount (except 'std') and round the result. Also remove the first row from the table.
        # Display the table on Streamlit along with a title.
        tbl = round(tbl * investment, 2)
        tbl['std'] = round(tbl['std']/investment, 2)
        tbl = tbl[1:10]
        st.write("Summary of the Investment Returns at the End of Three Years:")
        st.dataframe(tbl)

        # Create a statement about the CI and display it on Streamlit.
        ci_statement = f"There is a 95% chance that an investment of {investment} USD in the stock {ticker} will end within the range of {ci_lower} and {ci_upper} USD over the next 3 years."
        st.write(ci_statement)
        
    # Display a warning message that appears when the user enters an invalid stock ticker.
    except:
        st.warning("Oops, please enter a valid stock ticker!")

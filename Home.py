# Import the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import yfinance as yf
import plotly.express as px

st.set_page_config(
    page_title = "Stock Analysis Tool",
    page_icon = "💲",
)

st.sidebar.success("☝️Select a Feature From Above.")

# Create a title for the the web application
st.title("Stock Analysis Tool")

# Create a header and subheader
st.subheader("Welcome to the Stock Analysis Tool!")
st.write("There are several features available for use within this Stock Analysis Tool. Select a page from the left side of the screen for more details.")
st.write("We hope this web application can assist you in making more educated investment decisions!")

st.image("Images/finance.jpg")

st.write("Designed by Ikaika Smith and Tyler Johnson. Enjoy!")
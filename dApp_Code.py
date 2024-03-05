# Import the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import yfinance as yf
import plotly.express as px

from st_pages import Page, add_page_title, show_pages

## Declaring the pages in your app:

show_pages(
    [
        Page("Home.py", "Home Page", ":house:"),
        Page("Historical_Pricing.py", "Historical Pricing", ":chart:"),
        Page("Fundamental_Analysis.py", "Fundamental Analysis", ":books:"),
        Page("Forecasting.py", "Forecasting", ":pencil:"),
        Page("Stock_News.py", "Stock News", ":newspaper:"),
    ]
)
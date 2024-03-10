import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import requests

from stocknews import StockNews

st.title(":boom: Stock News Articles :boom:")

# Create a text input for the stock ticker
ticker = st.text_input("Stock Ticker")

sn = StockNews(ticker, save_news = False)
df =sn.read_rss()

if st.button("Give Me News"):
    for i in range(10):
        st.header(df["title"][i])
        st.subheader(df["published"][i])
        st.write(df["summary"][i])
        
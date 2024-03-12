"""
This page will allow the user to enter a stock ticker and obtain some of the most recent news articles relating to that company.

When an error occurs, or exception, Python will stop and generate an error message.
We will handle these exceptions using the try and except statements.
If the user enters an invalid ticker they will be asked to reenter a valid ticker rather than Python giving them an error message.
"""

# Import the required libraries and dependencies.
import streamlit as st
import yfinance as yf
import requests
import base64

# Display a title for the the stock news page.
st.title("📰 Stock News Articles")

# Display a subheader that explains the tool.
st.write("Enter a ticker below. The tool will obtain and display recent news articles for the company of your choice.")

st.divider()

# Create a text input for the user to enter a stock ticker.
ticker = st.text_input("⬇️ Enter a Stock Ticker")

# Only have the simulation run once the user clicks the "Give Me News" button.
if st.button("Give Me News"):
    # Create a catch-all (using try and except statements) in case the user enters an invalid stock ticker.
    try:
        # Create a variable that downloads data from yfinance using the ticker input.
        # Create a variable for just the stock news from yfinance.
        stock_data = yf.Ticker(ticker)
        stock_news = stock_data.news
        
        # Display a header for the news articles that appear.
        st.header(f"{ticker} News:")
        
        # Loop through the articles and display the titles, publishers, and article links.
        for i, article in enumerate(stock_news[:10]):  # Display up to 10 news articles
            col1, col2 = st.columns(2)
            with col1:
                thumbnail_data = article.get("thumbnail")
                if thumbnail_data and "resolutions" in thumbnail_data:
                    thumbnail_url = thumbnail_data["resolutions"][0]["url"]
                    try:
                        response = requests.get(thumbnail_url)
                        if response.status_code == 200:
                            image_data = response.content
                            encoded_image = base64.b64encode(image_data).decode()
                            st.image(f"data:image/png;base64,{encoded_image}")
                        else:
                            st.write("Failed to retrieve image. Status code:", response.status_code)
                    except Exception as e:
                        st.write("Error fetching image:", e)
                else:
                    st.write("No valid thumbnail image URL available for this article.")
            with col2:
                st.write("**TITLE:** ", stock_news[i]["title"])
                st.write("**PUBLISHER:** ", stock_news[i]["publisher"])
                st.write("**ARTICLE LINK:** ", stock_news[i]["link"])
            st.divider()
    
    # Display a warning message that appears when the user enters an invalid stock ticker.
    except:
        st.warning("Oops, please enter a valid stock ticker!")

# Import the required libraries.
import streamlit as st

# Configure the setup of the pages.
st.set_page_config(
    page_title = "Stock Analysis Tool",
    page_icon = "💲",
)

# Display a message on the sidebar telling the user to select one of the pages.
st.sidebar.success("☝️Select a Feature From Above.")

# Display a title for the the web application.
st.title("Stock Analysis Tool")

# Display a header and subheader.
st.subheader("Welcome to the Stock Analysis Tool!")
st.write("There are several features available for use within this Stock Analysis Tool. Select a page from the left side of the screen for more details.")
st.write("We hope this web application can assist you in making more educated investment decisions!")

# Display an image on the home page.
st.image("Images/finance.jpg")

# Display a statement giving credit to the designers of the app.
st.write("Designed by Ikaika Smith and Tyler Johnson. Enjoy!")

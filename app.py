import streamlit as st
from src.ui.pages import home, itinerary

# Sidebar Navigation
st.sidebar.title("🌍 Travel Assistant")
page = st.sidebar.radio("Go to", ["Home", "Itinerary"])

if page == "Home":
    home.home_page()
elif page == "Itinerary":
    itinerary.itinerary_page()

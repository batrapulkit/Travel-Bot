import streamlit as st
from src.data.weather_api import get_weather_forecast

def display_weather(destination, date):
    """Show weather forecast for selected date and destination."""
    weather = get_weather_forecast(destination, date)
    st.info(f"🌦 {weather['condition']} - {weather['temperature']}")

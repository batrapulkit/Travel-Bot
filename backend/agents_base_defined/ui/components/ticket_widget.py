import streamlit as st
from src.data.amadeus_api import get_ticket_prices

def display_tickets(destination, attractions):
    """Show available ticket prices for activities."""
    tickets = get_ticket_prices(destination, attractions)
    st.warning(f"🎟 Ticket Available: {tickets}")

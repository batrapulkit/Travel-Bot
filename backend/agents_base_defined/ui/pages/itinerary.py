import streamlit as st
from src.agentic.itinerary_planner import get_itinerary

def itinerary_page():
    """UI for generating and displaying a personalized itinerary."""
    st.title("🗺 Your Personalized Travel Itinerary")

    # User input fields
    destination = st.text_input("Enter Destination:", "Paris")
    start_date = st.date_input("Start Date:")
    duration = st.slider("Number of Days:", 1, 14, 3)
    
    # User Preferences (MCQ + Free Text)
    interests = st.multiselect("Select Interests:", ["Culture", "Food", "Adventure", "Shopping", "Nature", "Relaxation"])
    custom_interest = st.text_input("Other Interests:")
    if custom_interest:
        interests.append(custom_interest)
    
    budget = st.radio("Budget Level:", ["Low", "Medium", "High"])
    pace = st.radio("Travel Pace:", ["Relaxed", "Balanced", "Fast-Paced"])
    transport = st.radio("Preferred Transport:", ["Public Transport", "Car Rental", "Walking"])
    special_requests = st.text_area("Special Requests (optional):")

    if st.button("Generate Itinerary"):
        with st.spinner("Generating your personalized itinerary..."):
            itinerary = get_itinerary(destination, str(start_date), duration, interests, budget, pace, transport, special_requests)

        # Display itinerary
        for day in itinerary:
            st.subheader(f"📅 {day['date']}")
            st.write(f"**Morning:** {day['morning']}")
            st.write(f"**Afternoon:** {day['afternoon']}")
            st.write(f"**Evening:** {day['evening']}")
            if day["notes"]:
                st.warning(f"🎟 {day['notes']}")
            st.divider()

import streamlit as st

def home_page():
    """UI for Home Page with pre-built itineraries."""
    st.title("🌎 Smart Travel Planner")
    st.write("Plan your trip effortlessly with personalized itineraries!")

    # Pre-built itinerary options
    st.subheader("🔹 Pre-Built Itineraries")
    col1, col2 = st.columns(2)

    with col1:
        st.button("🇫🇷 3 Days in Paris", key="paris")
        st.button("🇯🇵 5 Days in Tokyo", key="tokyo")

    with col2:
        st.button("🇮🇹 4 Days in Rome", key="rome")
        st.button("🇺🇸 7 Days in New York", key="nyc")

    st.markdown("---")
    st.subheader("🔹 Create Your Own Itinerary")
    st.write("Want a custom trip? Click below to enter your preferences.")
    if st.button("📝 Start Planning"):
        st.switch_page("src/ui/pages/itinerary.py")

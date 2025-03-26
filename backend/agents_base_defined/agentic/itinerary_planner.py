import os
import sys
import random
from tabulate import tabulate

# Add the path to the data directory in sys.path to ensure local module is used
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, '..', 'data')  # Adjust path as per your folder structure
sys.path.insert(0, data_dir)  # Put the local module at the front of sys.path

# Now try importing from your custom weather_api module
try:
    from weather_api import get_weather  # Importing the function from your custom weather_api.py
except ImportError:
    print("❌ Could not import get_weather from local weather_api.py. Ensure the file is located in src/data/.")

# Your other import statements
from wikipedia_api import display_attractions

# Sample budget data
ACTIVITY_BUDGET = {
    "Street Food Tour": 20,
    "Wine Tasting": 30,
    "Cooking Class": 40,
    "National Park": 15,
    "Wildlife Safari": 50,
    "Skydiving": 150,
    "Rooftop Bar": 25,
    "Jazz Club": 35,
    "Museum Tour": 20,
    "Spa Retreat": 60
}

def generate_itinerary(destination, interests, days):
    """Generates a day-wise travel itinerary with activities, weather, and budget."""
    itinerary = []
    
    # Fetch top attractions using the Wikipedia API
    attractions = display_attractions(destination, interests).split("\n")[1:]
    
    for day in range(1, days + 1):
        if len(attractions) < days:
            random.shuffle(attractions)

        # Select 2-3 random activities per day
        daily_activities = random.sample(attractions, min(3, len(attractions)))
        
        # Calculate estimated budget
        daily_budget = sum(ACTIVITY_BUDGET.get(activity.strip(), 20) for activity in daily_activities)
        
        # Get weather forecast
        weather_info = get_weather(destination, str(day)) if 'get_weather' in globals() else "Weather info unavailable"
        
        itinerary.append({
            "Day": day,
            "Activities": daily_activities,
            "Weather": weather_info,
            "Estimated Budget": f"${daily_budget:.2f}"
        })
    
    return itinerary

def display_itinerary(itinerary):
    """Formats and prints the final itinerary."""
    print("\nYour Personalized Itinerary:\n")
    for day_plan in itinerary:
        print(f"🗓️ **Day {day_plan['Day']}**")
        print("📍 Activities:")
        for idx, activity in enumerate(day_plan['Activities'], start=1):
            print(f"   {idx}. {activity}")
        print(f"🌤️ Weather: {day_plan['Weather']}")
        print(f"💰 Estimated Budget: {day_plan['Estimated Budget']}\n")

def main():
    print("✨ Welcome to the Travel Planner ✈️")

    # User inputs
    destination = input("Enter your destination: ").strip()
    interests = input("Enter your interests (e.g., food, adventure, history): ").strip()
    days = int(input("How many days are you planning for? ").strip())

    if not destination or not interests or not days:
        print("❌ Please provide valid inputs.")
        return
    
    # Generate and display the itinerary
    itinerary = generate_itinerary(destination, interests, days)
    display_itinerary(itinerary)

if __name__ == "__main__":
    main()

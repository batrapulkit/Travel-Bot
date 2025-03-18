import requests
import os
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL", "http://api.weatherapi.com/v1/forecast.json")

def get_weather(destination, date):
    """
    Fetch real-time weather conditions for the given destination and date.
    If forecast data is unavailable, return current weather or show a more detailed error message.
    """
    try:
        params = {
            "key": WEATHER_API_KEY,
            "q": destination,
            "dt": date
        }
        response = requests.get(WEATHER_API_URL, params=params)
        data = response.json()

        # Debugging: Print the raw API response to inspect the structure of the data
        print("Raw API Response:", data)

        # Check if forecast data is available
        if "forecast" in data and "forecastday" in data["forecast"] and len(data["forecast"]["forecastday"]) > 0:
            weather_condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"].lower()
            return weather_condition
        elif "current" in data:  # If no forecast, use current weather and provide more detail
            weather_condition = data["current"]["condition"]["text"].lower()
            temperature = data["current"]["temp_c"]
            wind_speed = data["current"]["wind_kph"]
            humidity = data["current"]["humidity"]
            # Adding more detailed weather information
            return f"{weather_condition}, Temp: {temperature}°C, Wind: {wind_speed} kph, Humidity: {humidity}%"
        else:
            print(f"⚠️ No forecast or current weather data available for {destination} on {date}.")
            return "unknown"
    except Exception as e:
        print(f"⚠️ Weather API Error: {e}")
        return "unknown"

def filter_activities_by_weather(weather, activities, indoor_activities=None, outdoor_activities=None):
    """
    Filter activities based on weather conditions.
    """
    # Default values if not provided
    if indoor_activities is None:
        indoor_activities = ["Cooking Class", "Museum Visit", "Theater Show", "Shopping Mall"]
    if outdoor_activities is None:
        outdoor_activities = ["Hiking", "Beach Picnic", "Outdoor Market", "City Walking Tour"]
    
    if "rain" in weather or "storm" in weather or "snow" in weather:
        return [activity for activity in activities if activity in indoor_activities]
    else:
        return activities  # Keep all activities if weather is clear

# Predefined list of activities (no user input required)
activities = ["City Walking Tour", "Museum Visit", "Cooking Class", "Hiking"]

# Example usage
if __name__ == "__main__":
    # Fetch destination and date dynamically (e.g., user input or from a database)
    destination = input("Enter destination: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    weather = get_weather(destination, date)
    
    # Filter activities based on weather
    filtered_activities = filter_activities_by_weather(weather, activities)
    
    # Prepare data for tabular format
    table_data = [
        ["Destination", destination],
        ["Date", date],
        ["Weather", weather],
        ["Recommended Activities", ", ".join(filtered_activities)]
    ]
    
    # Print the table
    print("\nTravel Weather and Activities Recommendation:")
    print(tabulate(table_data, headers=["Property", "Value"], tablefmt="pretty"))

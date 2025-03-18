import requests
import os

class WeatherAgent:
    class WeatherAgent:
       def __init__(self):
        # Retrieve the weather API key from the environment variable
        self.api_key = os.getenv("WEATHER_API_KEY")  # Fetch API key from .env file
        self.base_url = "http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

        if not self.api_key:
            raise ValueError("API key is missing! Please add WEATHER_API_KEY to your .env file.")
        
    def get_weather(self, location):
        # Make a request to the weather API
        response = requests.get(f"{self.base_url}?key={self.api_key}&q={location}")
        if response.status_code == 200:
            data = response.json()
            # Extract relevant weather information from the response
            weather_info = {
                "location": data["location"]["name"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_kph"]
            }
            return weather_info
        else:
            return {"error": "Unable to fetch weather data."}

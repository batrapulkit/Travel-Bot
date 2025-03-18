import requests
import os
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv('WEATHER_API_KEY')

def get_weather(location: str, date: str):
    url = f"http://api.weatherapi.com/v1/history.json?key={weather_api_key}&q={location}&dt={date}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather = data['forecast']['forecastday'][0]['day']
            return {
                "temperature": weather['avgtemp_c'],
                "condition": weather['condition']['text'],
                "precipitation": weather['totalprecip_mm']
            }
        else:
            return None
    except Exception as e:
        print(f"Error with Weather API: {e}")
        return None

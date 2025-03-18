import requests
import os
from dotenv import load_dotenv

load_dotenv()

eventbrite_api_key = os.getenv('EVENTBRITE_API_KEY')

def search_events(location: str, date: str, interests: str):
    url = f"https://www.eventbriteapi.com/v3/events/search/"
    params = {
        "location.address": location,
        "start_date.range_start": date,
        "q": interests,
        "token": eventbrite_api_key
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200:
            return data.get('events', [])
        else:
            return []
    except Exception as e:
        print(f"Error with Eventbrite API: {e}")
        return []

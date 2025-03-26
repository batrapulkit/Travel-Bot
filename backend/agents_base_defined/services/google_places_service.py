import requests
import os
from dotenv import load_dotenv

load_dotenv()

google_places_api_key = os.getenv('GOOGLE_PLACES_API_KEY')

def search_places(query: str, location: str, radius: int = 5000):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": google_places_api_key
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200:
            return data.get('results', [])
        else:
            return []
    except Exception as e:
        print(f"Error with Google Places API: {e}")
        return []

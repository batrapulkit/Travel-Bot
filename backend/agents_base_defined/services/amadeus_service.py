import requests
import os
from dotenv import load_dotenv

load_dotenv()

amadeus_api_key = os.getenv('AMADEUS_API_KEY')
amadeus_api_secret = os.getenv('AMADEUS_API_SECRET')

def search_flights(origin: str, destination: str, departure_date: str):
    url = f"https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {
        "Authorization": f"Bearer {amadeus_api_key}"
    }
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if response.status_code == 200:
            return data['data']
        else:
            return []
    except Exception as e:
        print(f"Error with Amadeus API: {e}")
        return []

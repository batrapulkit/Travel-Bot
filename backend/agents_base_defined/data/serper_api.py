import requests
import os

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_API_URL = "https://api.serper.dev/search"

def search_places(query):
    headers = {
        'Authorization': f'Bearer {SERPER_API_KEY}',
    }
    params = {'query': query}
    response = requests.get(SERPER_API_URL, headers=headers, params=params)
    return response.json()

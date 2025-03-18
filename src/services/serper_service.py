import requests
import os
from dotenv import load_dotenv

load_dotenv()

serper_api_key = os.getenv('SERPER_API_KEY')

def search(query: str):
    url = f"https://api.serper.dev/search?q={query}&api_key={serper_api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data.get('organic', [])
        else:
            return []
    except Exception as e:
        print(f"Error with Serper API: {e}")
        return []

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys Dictionary
API_KEYS = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "WEATHER_API_KEY": os.getenv("WEATHER_API_KEY"),
    "SERPER_API_KEY": os.getenv("SERPER_API_KEY"),
    "AMADEUS_API_KEY": os.getenv("AMADEUS_API_KEY"),
    "AMADEUS_API_SECRET": os.getenv("AMADEUS_API_SECRET"),
    "GOOGLE_PLACES_API_KEY": os.getenv("GOOGLE_PLACES_API_KEY"),
    "EVENTBRITE_API_KEY": os.getenv("EVENTBRITE_API_KEY"),
}

def get_api_key(service_name):
    """Retrieve API key by service name."""
    key = API_KEYS.get(service_name)
    if not key:
        raise ValueError(f"Missing API key for {service_name}. Check your .env file.")
    return key

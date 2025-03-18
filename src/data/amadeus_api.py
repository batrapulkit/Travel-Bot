import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")

# Base URL for Amadeus API
TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_SEARCH_URL = "https://test.api.amadeus.com/v1/shopping/flight-offers"

def get_access_token():
    """
    Authenticate with Amadeus API and get an access token.
    Returns:
        str: Access token for API requests.
    Raises:
        RuntimeError: If authentication fails.
    """
    if not AMADEUS_API_KEY or not AMADEUS_API_SECRET:
        raise RuntimeError("❌ Amadeus API credentials are missing! Check your .env file.")

    payload = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(TOKEN_URL, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"❌ Authentication failed: {response.text}")
        raise RuntimeError("Failed to authenticate with Amadeus API.")

def get_ticket_prices(origin, destination, departure_date, return_date=None):
    """
    Fetch ticket prices using the Amadeus API.
    
    Args:
        origin (str): Departure airport code (e.g., "JFK").
        destination (str): Arrival airport code (e.g., "LHR").
        departure_date (str): Departure date in YYYY-MM-DD format.
        return_date (str, optional): Return date if it's a round trip.

    Returns:
        list: List of flight offers.
    """
    try:
        access_token = get_access_token()

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": 1
        }

        if return_date:
            params["returnDate"] = return_date

        response = requests.get(FLIGHT_SEARCH_URL, headers=headers, params=params)

        if response.status_code == 200:
            return response.json().get("data", [])
        
        elif response.status_code == 401:
            return {"error": "❌ Unauthorized - Check API Key & Subscription in Amadeus Portal."}

        else:
            return {"error": f"❌ Failed to fetch flight prices: {response.text}"}

    except requests.RequestException as e:
        return {"error": f"❌ Request Error: {e}"}

# Example Usage
if __name__ == "__main__":
    result = get_ticket_prices("JFK", "LHR", "2025-06-10")
    print(result) 

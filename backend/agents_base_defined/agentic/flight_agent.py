from src.data.amadeus_api import get_flights

class FlightAgent:
    def get_flights(self, origin, destination, departure_date):
        flights = get_flights(origin, destination, departure_date)
        if flights and 'data' in flights:
            return {"flights": flights['data']}
        return {"error": "No flights found"}

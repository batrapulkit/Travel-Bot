from src.data.serper_api import search_places
from src.data.wikipedia_api import get_wikipedia_summary

class DestinationAgent:
    def get_destination_info(self, query):
        places = search_places(query)
        if places:
            place_name = places['organic'][0]['title']
            description = get_wikipedia_summary(place_name)
            return {"place_name": place_name, "description": description}
        return {"error": "Destination not found"}

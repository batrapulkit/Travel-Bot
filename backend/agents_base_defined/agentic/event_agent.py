from src.data.serper_api import search_places

class EventAgent:
    def get_events(self, location):
        events = search_places(location + " events")
        if events:
            event_list = [event['title'] for event in events['organic']]
            return {"events": event_list}
        return {"error": "No events found"}

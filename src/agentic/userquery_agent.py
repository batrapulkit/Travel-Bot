# user_query_agent.py
from .travel_agent import TravelAgent
from .event_agent import EventAgent
from .flight_agent import FlightAgent
from .openai_service import OpenAIService
from .utils import format_response, handle_error

class UserQueryAgent:
    def __init__(self, openai_api_key):
        self.openai_service = OpenAIService(openai_api_key)
        self.travel_agent = TravelAgent(role="Travel Agent", goal="Assist with travel planning", attributes="helpful", llm=None, tools=[])
        self.event_agent = EventAgent(role="Event Agent", goal="Assist with events", attributes="helpful", llm=None, tools=[])
        self.flight_agent = FlightAgent(role="Flight Agent", goal="Assist with flight searches", attributes="helpful", llm=None, tools=[])

    def handle_query(self, query):
        """Handles user query and routes to appropriate agent."""
        try:
            if 'flight' in query:
                # Query related to flights
                return self.flight_agent.search_flights("current_location", "destination", "dates")
            elif 'event' in query:
                # Query related to events
                return self.event_agent.search_events("destination", "dates", "interests")
            elif 'weather' in query:
                # Query related to weather
                return self.travel_agent.gather_weather_info("destination", "dates")
            else:
                # Use OpenAI to respond to general queries
                return self.openai_service.generate_response(query)
        except Exception as e:
            return handle_error(e)

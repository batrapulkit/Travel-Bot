import requests
import random

def get_wikipedia_data(destination, query):
    """Fetches Wikipedia data dynamically for a given query related to the destination."""
    try:
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": f"{destination} {query}",
            "utf8": 1,
            "srlimit": 10  # Limit the number of results
        }
        response = requests.get(search_url, params=params)
        data = response.json()
        
        # Check if the response contains the 'search' results
        if 'query' in data and 'search' in data['query']:
            attractions = [item['title'] for item in data['query']['search']]
            return attractions
        else:
            return []
    except Exception as e:
        return [f"⚠️ Wikipedia API Error: {e}"]

def get_interest_based_attractions(interests):
    """Returns a list of attraction suggestions based on user interests."""
    interest_map = {
        "food": ["Street Food Tour", "Wine Tasting", "Cooking Class", "Food Festival", "Goan Cuisine Tasting"],
        "history": ["Ancient Ruins", "Heritage Walk", "Castle Visit", "Museum Tour", "Historic Monuments"],
        "nature": ["National Park", "Wildlife Safari", "Botanical Garden", "Mountain Trek", "Beach Picnic"],
        "adventure": ["Skydiving", "Bungee Jumping", "Mountain Climbing", "Paragliding", "Cave Exploration"],
        "relaxation": ["Spa Retreat", "Sunset Yoga", "Beach Picnic", "Meditation Retreat", "Nature Walk"],
        "nightlife": ["Rooftop Bar", "Jazz Club", "Night Cruise", "Night Market", "Dance Club"]
    }
    
    attractions = []
    for interest in interests.split(","):
        interest = interest.strip().lower()
        if interest in interest_map:
            attractions.extend(interest_map[interest])
    
    return attractions

def combine_attractions(destination, interests):
    """Combines both Wikipedia attractions and interest-based suggestions."""
    # Fetch Wikipedia attractions
    wikipedia_attractions = get_wikipedia_data(destination, "top attractions")
    
    # Get interest-based attractions
    interest_based_attractions = get_interest_based_attractions(interests)
    
    # Combine and remove duplicates
    all_attractions = list(set(wikipedia_attractions + interest_based_attractions))
    
    # Shuffle and limit the result to 10
    random.shuffle(all_attractions)
    return all_attractions[:10]

def display_attractions(destination, interests):
    """Displays top attractions after combining results from Wikipedia and interests."""
    attractions = combine_attractions(destination, interests)
    
    if attractions:
        formatted_output = f"\nTop Attractions for {destination} based on your interests:\n"
        formatted_output += "\n".join([f"{idx + 1}. {attraction}" for idx, attraction in enumerate(attractions)])
        return formatted_output
    else:
        return f"No attractions found for {destination}. Try again later."

def main():
    print("Welcome to the Travel Planner!")
    
    # Get user input for destination and interests
    destination = input("Enter destination: ").strip()
    interests = input("Enter your interests (comma separated, e.g., food, history, nature): ").strip()
    
    if not destination or not interests:
        print("❌ Destination and interests are required. Please try again.")
        return
    
    # Fetch and display the top attractions
    attractions = display_attractions(destination, interests)
    
    # Print the result
    print(attractions)

if __name__ == "__main__":
    main()

from datetime import datetime
from dotenv import load_dotenv

from domain.vacation_period_calculator import VacationPeriodCalculator
from domain.travel_combination_generator import TravelCombinationGenerator
from domain.travel_formatter import TravelFormatter
from domain.cheapest_trip_finder import CheapestTripFinder

from application.flight_search_service import FlightSearchService
from application.search_result_displayer import format_cheapest_trips
from application.search_mapping import map_search

from infrastructure.serp_api.serp_api_client import SerpApiClient
from infrastructure.serp_api.serp_api_flight_provider import SerpApiFlightProvider
from infrastructure.historic.flight_search_database import FlightSearchDatabase

load_dotenv()

#Initiate my DB
db = FlightSearchDatabase()

# I first need the starting date, the trip duration, and the search period:
start_date_str = input("When do you want to go? (YYYY-MM-DD) ")
stay_duration_days = int(input("For how long? (in days) "))
search_period_days = int(input("Which period do you want to search for the best price? (in days) "))

start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

# I use my VacationPeriodCalculator to know all the departure dates that fit in the user’s search period:
possible_departures = VacationPeriodCalculator.generate_possible_departures(
    search_start_date=start_date,
    stay_duration_days=stay_duration_days,
    search_period_days=search_period_days
)

# Now I have a list of date objects, each representing a valid start date for the trip.
# I use my TravelCombinationGenerator to get (departure, return) tuples:
combination_generator = TravelCombinationGenerator(stay_duration_days=stay_duration_days)
trip_combinations = combination_generator.generate(possible_departures)

# I use TravelFormatter to add the origin and destination so my API service knows what to call:
origin = input("Departure airport code: ")
destination = input("Arrival airport code: ")

mapped_search = map_search(origin, destination, stay_duration_days, search_period_days)
search_id = db.insert_search(mapped_search)

trips = TravelFormatter.format_combinations(trip_combinations, origin, destination)

# Finally, I use my FlightSearchService:
serp_api_client = SerpApiClient()
serp_api_provider = SerpApiFlightProvider(serp_api_client)
flight_service = FlightSearchService(serp_api_provider)

trips_with_prices = flight_service.search_flight(trips)
cheapest_trip, average_price = CheapestTripFinder.find_cheapest(trips_with_prices)
for trip in trips_with_prices:
    if trip["price"] is not None:
        db.insert_result(trip, search_id, "serp_api")

print(format_cheapest_trips(cheapest_trip, average_price))
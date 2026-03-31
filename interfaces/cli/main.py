from datetime import datetime
from dotenv import load_dotenv
from domain.vacation_period_calculator import VacationPeriodCalculator
from domain.travel_combination_generator import TravelCombinationGenerator
from domain.travel_formatter import TravelFormatter
from infrastructure.amadeus_client import AmadeusClient
from application.flight_search_service import FlightSearchService
from infrastructure.cache.hybrid_flight_cache import HybridFlightCache
from domain.cheapest_trip_finder import CheapestTripFinder
from application.search_result_displayer import format_cheapest_trips

load_dotenv()
cache = HybridFlightCache()

#I first need the starting date, the trip duration, and the search period:

start_date_str = input("When do you want to go? (YYYY-MM-DD) ")
stay_duration_days = int(input("For how long? (in days) "))
search_period_days = int(input("Which period do you want to search for the best price? (in days) "))

start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

#I use my VacationPeriodCalculator to know all the departure dates that fit in the user’s search period:
possible_departures = VacationPeriodCalculator.generate_possible_departures(
    search_start_date=start_date,
    stay_duration_days=stay_duration_days,
    search_period_days=search_period_days
)

#Now I have a list of date objects, each representing a valid start date for the trip.
#I use my TravelCombinationGenerator to get (departure, return) tuples:
combination_generator = TravelCombinationGenerator(stay_duration_days=stay_duration_days)
trip_combinations = combination_generator.generate(possible_departures)

#I use TravelFormatter to add the origin and destination so my API service knows what to call:
origin = input("Departure airport code: ")
destination = input("Arrival airport code: ")

trips = TravelFormatter.format_combinations(trip_combinations, origin, destination)

#Finally, I use my FlightSearchService:
amadeus_client = AmadeusClient()
flight_service = FlightSearchService(amadeus_client, cache=cache)

trips_with_prices =flight_service.search_flight(trips)
cheapest_trip, average_price = CheapestTripFinder.find_cheapest(trips_with_prices)

print(format_cheapest_trips(cheapest_trip, average_price))

'''
When do you want to go? (YYYY-MM-DD) 2026-03-09
For how long? (in days) 21
Which period do you want to search for the best price? (in days) 30
Departure airport code: ICN
Arrival airport code: CDG
'''
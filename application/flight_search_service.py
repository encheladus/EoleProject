import logging

from application.cache_key_builder import build_cache_key
from infrastructure.amadeus_client import AmadeusClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlightSearchService:

    def __init__(self, amadeus_client, cache=None):
        self.client = amadeus_client.get_client()
        self.cache = cache #Injected dependances

    def search_flight(self, trips):
        for trip in trips:
            departure_date = trip["departure_date"]
            return_date = trip["return_date"]
            destination = trip["destination"]
            origin = trip["origin"]

            key = build_cache_key(origin, destination, departure_date, return_date)

            if self.cache and self.cache.has(key):
                trip["price"] = self.cache.get(key)
                logger.info(f"Cache hit for {origin}->{destination}: {trip['price']}")
                continue

            # --- Step 1: prepare the API call parameters ---
            params_amadeus = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": departure_date,
                "returnDate": return_date,
                "adults": 1  # minimal example
            }

            # --- Step 2: Calling amadeus API with error handling ---
            try:
                response = self.client.shopping.flight_offers_search.get(**params_amadeus)
                if response.data:
                    trip["price"] = response.data[0]["price"].get("total", None)
                    logger.info(f"Flight found for {origin}->{destination}: {trip['price']}")
                else:
                    trip["price"] = None  # no flights found
                    logger.warning(f"No flight found for {origin}->{destination}")
            except Exception as e:
                trip["price"] = None
                # optional: log the exception for debugging
                logger.error(f"Error fetching flight for {origin}->{destination}: {e}")

            if self.cache:
                self.cache.set(key, trip["price"])

        return trips
import logging
from infrastructure.amadeus_client import AmadeusClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlightSearchService:

    def __init__(self, amadeus_client):
        self.client = amadeus_client.get_client()

    def search_flight(self, trips):
        for trip in trips:
            departure_date = trip["departure_date"]
            return_date = trip["return_date"]
            destination = trip["destination"]
            origin = trip["origin"]

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
                response = self.client.shopping.flight_offers.get(**params_amadeus)
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

        return trips
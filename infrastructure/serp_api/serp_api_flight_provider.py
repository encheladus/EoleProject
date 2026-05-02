import logging
from serpapi.google_search import GoogleSearch

from domain.flight_offer import FlightOffer
from infrastructure.serp_api.serp_api_mapping import map_serpapi_to_offers

logger = logging.getLogger(__name__)


class SerpApiFlightProvider:
    def __init__(self, serp_api_client):
        self.api_key = serp_api_client.get_client()

    def search_offer(
        self,
        origin: str,
        destination: str,
        departure_date: str,
        return_date: str,
    ) -> FlightOffer | None:
        try:
            search = GoogleSearch({
                "engine": "google_flights",
                "departure_id": origin,
                "arrival_id": destination,
                "currency": "EUR",
                "type": "1",
                "outbound_date": departure_date,
                "return_date": return_date,
                "api_key": self.api_key,
                "no_cache": True,
                "hl": "en",
                "stops": 1,
                "exclude_conns": "DOH,AUH,MCT,RUH,JED,KWI,BAH"
            })

            results = search.get_dict()

            error = results.get("error")

            print("STATUS:", results.get("search_metadata", {}).get("status"))
            print("ERROR:", error)
            print("URL:", results.get("search_metadata", {}).get("google_flights_url"))

            if error:
                logger.warning(f"SerpApi error for {origin}->{destination}: {error}")
                return None

            offers = map_serpapi_to_offers(results)

            if not offers:
                logger.warning(f"No flight found for {origin}->{destination}")
                return None

            cheapest = min(offers, key=lambda x: x.price)

            return cheapest

        except Exception as e:
            logger.exception(f"Error fetching flight: {e}")
            return None
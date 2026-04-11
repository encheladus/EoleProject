import logging
from serpapi import GoogleSearch

from domain.flight_offer import FlightOffer

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

            status = results.get("search_metadata", {}).get("status")
            error = results.get("error")

            print("STATUS:", status)
            print("ERROR:", error)
            print("URL:", results.get("search_metadata", {}).get("google_flights_url"))

            if error:
                logger.warning(f"SerpApi error for {origin}->{destination}: {error}")
                return None

            best_flights = results.get("best_flights", [])
            other_flights = results.get("other_flights", [])
            all_flights = best_flights + other_flights

            print("BEST:", len(best_flights), "OTHER:", len(other_flights))

            if not all_flights:
                logger.warning(f"No flight found for {origin}->{destination}")
                return None

            cheapest = min(all_flights, key=lambda x: x.get("price", float("inf")))
            raw_price = cheapest.get("price")

            if raw_price is None:
                logger.warning(f"No price found for {origin}->{destination}")
                return None

            return FlightOffer(
                price=float(raw_price),
                booking_link = results.get("search_metadata", {}).get("google_flights_url"),
            )

        except Exception as e:
            logger.exception(f"Error fetching flight: {e}")
            return None
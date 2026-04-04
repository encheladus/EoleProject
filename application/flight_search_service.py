import logging

from application.cache_key_builder import build_cache_key

logger = logging.getLogger(__name__)


class FlightSearchService:
    def __init__(self, provider, cache=None):
        self.provider = provider
        self.cache = cache

    def search_flight(self, trips: list[dict]) -> list[dict]:
        for trip in trips:
            departure_date = trip["departure_date"]
            return_date = trip["return_date"]
            destination = trip["destination"]
            origin = trip["origin"]

            key = build_cache_key(origin, destination, departure_date, return_date)

            offer = None

            if self.cache and self.cache.has(key):
                offer = self.cache.get(key)
                logger.info(f"Cache hit for {origin}->{destination}")

            else:
                offer = self.provider.search_offer(
                    origin=origin,
                    destination=destination,
                    departure_date=departure_date,
                    return_date=return_date,
                )

                if self.cache:
                    self.cache.set(key, offer)

            if offer:
                trip["price"] = offer.price
                trip["booking_link"] = offer.booking_link
                logger.info(
                    f"Flight found for {origin}->{destination}: {offer.price}, link: {offer.booking_link}"
                )
            else:
                trip["price"] = None
                trip["booking_link"] = None
                logger.warning(f"No flight found for {origin}->{destination}")

        return trips
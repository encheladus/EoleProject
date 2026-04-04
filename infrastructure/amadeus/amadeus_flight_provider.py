import logging

from domain.flight_offer import FlightOffer

logger = logging.getLogger(__name__)


class AmadeusFlightProvider:
    def __init__(self, amadeus_client):
        self.client = amadeus_client.get_client()

    def search_offer(
        self,
        origin: str,
        destination: str,
        departure_date: str,
        return_date: str,
    ) -> FlightOffer | None:
        params_amadeus = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
        }

        try:
            response = self.client.shopping.flight_offers_search.get(**params_amadeus)

            if not response.data:
                logger.warning(f"No flight found for {origin}->{destination}")
                return None

            first_offer = response.data[0]

            raw_price = first_offer.get("price", {}).get("total")
            if raw_price is None:
                logger.warning(f"No price found for {origin}->{destination}")
                return None

            price = float(raw_price)

            booking_link = (
                first_offer.get("link", {}).get("href")
                or "https://www.google.com/travel/flights"
            )

            logger.info(
                f"Flight found for {origin}->{destination}: {price}, link: {booking_link}"
            )

            return FlightOffer(
                price=price,
                booking_link=booking_link,
            )

        except Exception as e:
            logger.error(f"Error fetching flight for {origin}->{destination}: {e}")
            return None
from typing import Protocol

from domain.flight_offer import FlightOffer


class FlightProvider(Protocol):
    def search_offer(
            self,
            origin: str,
            destination: str,
            departure_date: str,
            return_date: str,
    ) -> FlightOffer | None:
        ...
from domain.flight_offer import FlightOffer


def map_serpapi_to_offers(results: dict) -> list[FlightOffer]:
    flights = results.get("best_flights") or results.get("other_flights") or []

    offers = []

    for flight in flights:
        price = flight.get("price")

        if not price:
            continue

        booking_link = (
            results.get("search_metadata", {}).get("google_flights_url")
        )

        offers.append(
            FlightOffer(
                price=float(price),
                booking_link=booking_link,
            )
        )

    return offers
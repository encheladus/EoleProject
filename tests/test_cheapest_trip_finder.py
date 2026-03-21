from domain.cheapest_trip_finder import CheapestTripFinder


def test_find_cheapest_normal_case():
    trips = [
        {
            "departure_date": "2026-03-09",
            "return_date": "2026-03-30",
            "origin": "CDG",
            "destination": "ICN",
            "price": "950.00"
        },
        {
            "departure_date": "2026-03-10",
            "return_date": "2026-03-31",
            "origin": "CDG",
            "destination": "ICN",
            "price": "870.00"
        },
        {
            "departure_date": "2026-03-11",
            "return_date": "2026-04-01",
            "origin": "CDG",
            "destination": "ICN",
            "price": "910.00"
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert result["price"] == "870.00"
    assert result["departure_date"] == "2026-03-10"
    assert result["return_date"] == "2026-03-31"


def test_find_cheapest_single_valid_trip():
    trips = [
        {
            "departure_date": "2026-03-09",
            "return_date": "2026-03-30",
            "origin": "CDG",
            "destination": "ICN",
            "price": None
        },
        {
            "departure_date": "2026-03-10",
            "return_date": "2026-03-31",
            "origin": "CDG",
            "destination": "ICN",
            "price": "870.00"
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert result["price"] == "870.00"
    assert result["departure_date"] == "2026-03-10"


def test_find_cheapest_no_valid_trip():
    trips = [
        {
            "departure_date": "2026-03-09",
            "return_date": "2026-03-30",
            "origin": "CDG",
            "destination": "ICN",
            "price": None
        },
        {
            "departure_date": "2026-03-10",
            "return_date": "2026-03-31",
            "origin": "CDG",
            "destination": "ICN",
            "price": None
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert result is None
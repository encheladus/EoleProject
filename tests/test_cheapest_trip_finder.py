from domain.cheapest_trip_finder import CheapestTripFinder


def test_find_cheapest_returns_all_cheapest_trips():
    trips = [
        {
            "departure_date": "2026-05-09",
            "return_date": "2026-05-30",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        },
        {
            "departure_date": "2026-05-10",
            "return_date": "2026-05-31",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        },
        {
            "departure_date": "2026-05-11",
            "return_date": "2026-06-01",
            "origin": "ICN",
            "destination": "CDG",
            "price": "300.00"
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    expected = [
        {
            "departure_date": "2026-05-09",
            "return_date": "2026-05-30",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        },
        {
            "departure_date": "2026-05-10",
            "return_date": "2026-05-31",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        }
    ]

    assert result == expected


def test_find_cheapest_ignores_none_prices():
    trips = [
        {
            "departure_date": "2026-05-09",
            "return_date": "2026-05-30",
            "origin": "ICN",
            "destination": "CDG",
            "price": None
        },
        {
            "departure_date": "2026-05-10",
            "return_date": "2026-05-31",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        },
        {
            "departure_date": "2026-05-11",
            "return_date": "2026-06-01",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert len(result) == 2
    assert all(trip["price"] == "214.59" for trip in result)


def test_find_cheapest_returns_single_trip_if_only_one_cheapest():
    trips = [
        {
            "departure_date": "2026-05-09",
            "return_date": "2026-05-30",
            "origin": "ICN",
            "destination": "CDG",
            "price": "400.00"
        },
        {
            "departure_date": "2026-05-10",
            "return_date": "2026-05-31",
            "origin": "ICN",
            "destination": "CDG",
            "price": "214.59"
        },
        {
            "departure_date": "2026-05-11",
            "return_date": "2026-06-01",
            "origin": "ICN",
            "destination": "CDG",
            "price": "300.00"
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert len(result) == 1
    assert result[0]["price"] == "214.59"
    assert result[0]["departure_date"] == "2026-05-10"


def test_find_cheapest_returns_none_if_no_valid_price():
    trips = [
        {
            "departure_date": "2026-05-09",
            "return_date": "2026-05-30",
            "origin": "ICN",
            "destination": "CDG",
            "price": None
        },
        {
            "departure_date": "2026-05-10",
            "return_date": "2026-05-31",
            "origin": "ICN",
            "destination": "CDG",
            "price": None
        }
    ]

    result = CheapestTripFinder.find_cheapest(trips)

    assert result is None
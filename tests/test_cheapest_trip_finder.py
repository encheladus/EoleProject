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

    cheapest_trips, average_price = CheapestTripFinder.find_cheapest(trips)

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

    assert cheapest_trips == expected
    assert average_price == round((214.59 + 214.59 + 300.00) / 3, 2)


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

    cheapest_trips, average_price = CheapestTripFinder.find_cheapest(trips)

    assert len(cheapest_trips) == 2
    assert all(trip["price"] == "214.59" for trip in cheapest_trips)
    assert average_price == 214.59


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

    cheapest_trips, average_price = CheapestTripFinder.find_cheapest(trips)

    assert len(cheapest_trips) == 1
    assert cheapest_trips[0]["price"] == "214.59"
    assert cheapest_trips[0]["departure_date"] == "2026-05-10"
    assert average_price == (400.00 + 214.59 + 300.00) / 3


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

    cheapest_trips, average_price = CheapestTripFinder.find_cheapest(trips)

    assert cheapest_trips is None
    assert average_price is None
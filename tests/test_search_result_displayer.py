from application.search_result_displayer import format_cheapest_trips

def test_format_cheapest_trips():
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
        }
        ]

    result = format_cheapest_trips(trips, 400.00)
    assert 'ICN' in result
    assert 'CDG' in result
    assert '2026-05-09' in result
    assert '2026-05-30' in result
    assert '2026-05-10' in result
    assert '2026-05-31' in result
    assert '214.59' in result
    assert '400.00' in result
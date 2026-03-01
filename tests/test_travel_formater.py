from datetime import date
from domain.travel_formatter import TravelFormatter

def test_format_combinations_normal():
    combinations = [
        (date(2026, 1, 1), date(2026, 1, 15)),
        (date(2026, 1, 2), date(2026, 1, 16)),
    ]

    result = TravelFormatter.format_combinations(
        combinations,
        origin="Paris",
        destination="Seoul"
    )

    expected = [
        {
            "departure_date": "2026-01-01",
            "return_date": "2026-01-15",
            "destination": "Seoul",
            "origin": "Paris",
            "price": None
        },
        {
            "departure_date": "2026-01-02",
            "return_date": "2026-01-16",
            "destination": "Seoul",
            "origin": "Paris",
            "price": None
        }
    ]

    assert result == expected

def test_format_combinations_empty():
    result = TravelFormatter.format_combinations(
        [],
        origin="Paris",
        destination="Seoul"
    )

    assert result == []

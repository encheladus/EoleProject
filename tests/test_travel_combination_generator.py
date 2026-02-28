import pytest
from datetime import date, timedelta
from domain.travel_combination_generator import TravelCombinationGenerator


def test_generate_travel_combinations_normal():
    generator = TravelCombinationGenerator(stay_duration_days=14)
    departure_dates = [date(2026, 1, 1), date(2026, 1, 2)]

    result = generator.generate(departure_dates)

    expected = [
        (date(2026, 1, 1), date(2026, 1, 15)),
        (date(2026, 1, 2), date(2026, 1, 16)),
    ]
    assert result == expected


def test_generate_travel_combinations_empty_list():
    generator = TravelCombinationGenerator(stay_duration_days=14)
    result = generator.generate([])
    assert result == []


def test_invalid_duration_raises_error():
    with pytest.raises(ValueError):
        TravelCombinationGenerator(stay_duration_days=0)
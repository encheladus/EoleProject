import pytest
from datetime import date, timedelta
from domain.vacation_period_calculator import VacationPeriodCalculator


def test_generate_possible_departures_normal_case():
    search_start = date(2026, 1, 1)
    stay_duration = 10
    search_period = 30

    result = VacationPeriodCalculator.generate_possible_departures(
        search_start,
        stay_duration,
        search_period
    )

    # Manual calculation needed
    search_end = search_start + timedelta(days=search_period)

    expected = []
    current = search_start
    while current + timedelta(days=stay_duration) <= search_end:
        expected.append(current)
        current += timedelta(days=1)

    assert result == expected


def test_generate_possible_departures_no_possible_dates():
    search_start = date(2026, 1, 1)
    stay_duration = 20
    search_period = 10  # trop court

    result = VacationPeriodCalculator.generate_possible_departures(
        search_start,
        stay_duration,
        search_period
    )

    assert result == []


def test_generate_possible_departures_invalid_stay_duration():
    search_start = date(2026, 1, 1)

    with pytest.raises(ValueError):
        VacationPeriodCalculator.generate_possible_departures(
            search_start,
            0,
            30
        )


def test_generate_possible_departures_invalid_search_period():
    search_start = date(2026, 1, 1)

    with pytest.raises(ValueError):
        VacationPeriodCalculator.generate_possible_departures(
            search_start,
            10,
            0
        )
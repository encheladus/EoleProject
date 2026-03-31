import pytest
from datetime import date
from domain.date_range_generator import DateRangeGenerator

# Normal case → plusieurs dates
# Limit case → start = end
# Error case → start > end

def test_generate_dates_normal():
    start = date(2026, 2, 10)
    end = date(2026, 2, 12)
    result = DateRangeGenerator.generate_departure_dates(start, end)
    expected = [date(2026, 2, 10), date(2026, 2, 11), date(2026, 2, 12)]
    assert result == expected

def test_generate_dates_limit():
    start = date(2026, 2, 12)
    end = date(2026, 2, 12)
    result = DateRangeGenerator.generate_departure_dates(start, end)
    expected = [date(2026, 2, 12)]
    assert result == expected

def test_generate_dates_error():
    start = date(2026, 2, 13)
    end = date(2026, 2, 12)
    with pytest.raises(ValueError) as excinfo:
            DateRangeGenerator.generate_departure_dates(start, end)
    assert str(excinfo.value) == "start_date cannot be after end_date"

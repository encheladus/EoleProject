import pytest
from unittest.mock import MagicMock

from application.flight_search_service import FlightSearchService
from domain.flight_offer import FlightOffer


@pytest.fixture
def mock_provider():
    return MagicMock()


def test_search_flight_success(mock_provider):
    mock_provider.search_offer.return_value = FlightOffer(
        price=123.45,
        booking_link="https://booking.test/offer-1",
    )

    service = FlightSearchService(provider=mock_provider)

    trips = [
        {
            "departure_date": "2026-04-01",
            "return_date": "2026-04-05",
            "origin": "CDG",
            "destination": "LON",
        }
    ]

    result = service.search_flight(trips)

    assert result[0]["price"] == 123.45
    assert result[0]["booking_link"] == "https://booking.test/offer-1"

    mock_provider.search_offer.assert_called_once_with(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )


def test_search_flight_no_data(mock_provider):
    mock_provider.search_offer.return_value = None

    service = FlightSearchService(provider=mock_provider)

    trips = [
        {
            "departure_date": "2026-04-01",
            "return_date": "2026-04-05",
            "origin": "CDG",
            "destination": "LON",
        }
    ]

    result = service.search_flight(trips)

    assert result[0]["price"] is None
    assert result[0]["booking_link"] is None


def test_search_flight_exception(mock_provider):
    # Le provider est censé absorber ses exceptions et retourner None,
    # donc ici on simule le comportement final attendu du provider.
    mock_provider.search_offer.return_value = None

    service = FlightSearchService(provider=mock_provider)

    trips = [
        {
            "departure_date": "2026-04-01",
            "return_date": "2026-04-05",
            "origin": "CDG",
            "destination": "LON",
        }
    ]

    result = service.search_flight(trips)

    assert result[0]["price"] is None
    assert result[0]["booking_link"] is None


def test_search_flight_cache_hit(mock_provider):
    mock_cache = MagicMock()
    mock_cache.has.return_value = True
    mock_cache.get.return_value = FlightOffer(
        price=999.99,
        booking_link="https://booking.test/cached-offer",
    )

    service = FlightSearchService(provider=mock_provider, cache=mock_cache)

    trips = [
        {
            "departure_date": "2026-04-01",
            "return_date": "2026-04-05",
            "origin": "CDG",
            "destination": "LON",
        }
    ]

    result = service.search_flight(trips)

    assert result[0]["price"] == 999.99
    assert result[0]["booking_link"] == "https://booking.test/cached-offer"

    mock_provider.search_offer.assert_not_called()


def test_search_flight_cache_miss(mock_provider):
    mock_cache = MagicMock()
    mock_cache.has.return_value = False

    offer = FlightOffer(
        price=123.45,
        booking_link="https://booking.test/offer-1",
    )
    mock_provider.search_offer.return_value = offer

    service = FlightSearchService(provider=mock_provider, cache=mock_cache)

    trips = [
        {
            "departure_date": "2026-04-01",
            "return_date": "2026-04-05",
            "origin": "CDG",
            "destination": "LON",
        }
    ]

    result = service.search_flight(trips)

    assert result[0]["price"] == 123.45
    assert result[0]["booking_link"] == "https://booking.test/offer-1"

    mock_cache.set.assert_called_once()
    cached_key, cached_offer = mock_cache.set.call_args.args
    assert cached_offer == offer
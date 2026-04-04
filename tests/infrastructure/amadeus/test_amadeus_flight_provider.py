import pytest
from unittest.mock import MagicMock

from infrastructure.amadeus.amadeus_flight_provider import AmadeusFlightProvider
from domain.flight_offer import FlightOffer


@pytest.fixture
def mock_amadeus_client():
    mock_client_instance = MagicMock()

    mock_amadeus_client = MagicMock()
    mock_amadeus_client.get_client.return_value = mock_client_instance

    return mock_amadeus_client


def test_search_offer_success(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.return_value.data = [
        {
            "price": {"total": "123.45"},
            "link": {"href": "https://booking.test/amadeus-offer"},
        }
    ]

    provider = AmadeusFlightProvider(mock_amadeus_client)

    result = provider.search_offer(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )

    assert isinstance(result, FlightOffer)
    assert result.price == 123.45
    assert result.booking_link == "https://booking.test/amadeus-offer"


def test_search_offer_no_data(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.return_value.data = []

    provider = AmadeusFlightProvider(mock_amadeus_client)

    result = provider.search_offer(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )

    assert result is None


def test_search_offer_exception(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.side_effect = Exception("API down")

    provider = AmadeusFlightProvider(mock_amadeus_client)

    result = provider.search_offer(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )

    assert result is None


def test_search_offer_missing_link_uses_fallback(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.return_value.data = [
        {
            "price": {"total": "123.45"},
        }
    ]

    provider = AmadeusFlightProvider(mock_amadeus_client)

    result = provider.search_offer(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )

    assert isinstance(result, FlightOffer)
    assert result.price == 123.45
    assert result.booking_link == "https://www.google.com/travel/flights"


def test_search_offer_missing_price_returns_none(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.return_value.data = [
        {
            "price": {},
            "link": {"href": "https://booking.test/amadeus-offer"},
        }
    ]

    provider = AmadeusFlightProvider(mock_amadeus_client)

    result = provider.search_offer(
        origin="CDG",
        destination="LON",
        departure_date="2026-04-01",
        return_date="2026-04-05",
    )

    assert result is None
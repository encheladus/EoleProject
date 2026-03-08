import pytest
from unittest.mock import MagicMock
from infrastructure.flight_search_service import FlightSearchService

@pytest.fixture
def mock_amadeus_client():
    # mock the client returned by get_client()
    mock_client_instance = MagicMock()
    mock_client_instance.shopping.flight_offers_search.get.return_value.data = [
        {"price": {"total": "123.45"}}
    ]

    # mock the AmadeusClient itself
    mock_amadeus_client = MagicMock()
    mock_amadeus_client.get_client.return_value = mock_client_instance

    return mock_amadeus_client

def test_search_flight_success(mock_amadeus_client):
    service = FlightSearchService(mock_amadeus_client)
    trips = [
        {"departure_date": "2026-04-01", "return_date": "2026-04-05", "origin": "CDG", "destination": "LON"}
    ]
    result = service.search_flight(trips)
    assert result[0]["price"] == "123.45"

def test_search_flight_no_data(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.return_value.data = []

    service = FlightSearchService(mock_amadeus_client)
    trips = [
        {"departure_date": "2026-04-01", "return_date": "2026-04-05", "origin": "CDG", "destination": "LON"}
    ]
    result = service.search_flight(trips)
    assert result[0]["price"] is None

def test_search_flight_exception(mock_amadeus_client):
    mock_amadeus_client.get_client.return_value.shopping.flight_offers_search.get.side_effect = Exception("API down")

    service = FlightSearchService(mock_amadeus_client)
    trips = [
        {"departure_date": "2026-04-01", "return_date": "2026-04-05", "origin": "CDG", "destination": "LON"}
    ]
    result = service.search_flight(trips)
    assert result[0]["price"] is None
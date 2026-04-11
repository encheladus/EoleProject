from unittest.mock import MagicMock
import pytest

from infrastructure.serp_api.serp_api_flight_provider import SerpApiFlightProvider
from domain.flight_offer import FlightOffer


@pytest.fixture
def mock_client():
    wrapper = MagicMock()
    wrapper.get_client.return_value = "fake_api_key"
    return wrapper


def test_search_offer_success(monkeypatch, mock_client):
    fake_response = {
        "best_flights": [{"price": 300}],
        "other_flights": [{"price": 250}],
    }

    class FakeSearch:
        def __init__(self, params):
            self.params = params

        def get_dict(self):
            return fake_response

    monkeypatch.setattr(
        "infrastructure.serp_api.serp_api_flight_provider.GoogleSearch",
        FakeSearch
    )

    provider = SerpApiFlightProvider(mock_client)

    result = provider.search_offer("CDG", "ICN", "2026-06-01", "2026-06-15")

    assert isinstance(result, FlightOffer)
    assert result.price == 250.0


def test_search_offer_no_result(monkeypatch, mock_client):
    class FakeSearch:
        def __init__(self, params):
            pass

        def get_dict(self):
            return {}

    monkeypatch.setattr(
        "infrastructure.serp_api.serp_api_flight_provider.GoogleSearch",
        FakeSearch
    )

    provider = SerpApiFlightProvider(mock_client)

    result = provider.search_offer("CDG", "ICN", "2026-06-01", "2026-06-15")

    assert result is None
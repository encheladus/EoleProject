import json
import time
from unittest.mock import patch, mock_open

from infrastructure.cache.persistent_flight_cache import PersistentFlightCache
from domain.flight_offer import FlightOffer


def test_persistent_set_and_get():
    offer = FlightOffer(price=100.0, booking_link="https://test.com")

    mock_file = mock_open()

    with patch("builtins.open", mock_file), patch("pathlib.Path.exists", return_value=False):
        PersistentFlightCache.set("key1", offer)
        mock_file().write.assert_called()

    written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
    loaded_data = json.loads(written_data)

    with patch("builtins.open", mock_open(read_data=json.dumps(loaded_data))), \
         patch("pathlib.Path.exists", return_value=True):
        result = PersistentFlightCache.get("key1")

    assert isinstance(result, FlightOffer)
    assert result.price == 100.0
    assert result.booking_link == "https://test.com"


def test_persistent_expiration():
    timestamp_old = time.time() - (PersistentFlightCache._ttl + 10)
    data = {
        "key2": [
            {
                "price": 200.0,
                "booking_link": "https://expired.com"
            },
            timestamp_old
        ]
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(data))), \
         patch("pathlib.Path.exists", return_value=True), \
         patch("infrastructure.cache.persistent_flight_cache.PersistentFlightCache._save") as mock_save:
        result = PersistentFlightCache.get("key2")

    assert result is None
    mock_save.assert_called_once()
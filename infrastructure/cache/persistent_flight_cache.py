import json
import time
from pathlib import Path

from domain.flight_offer import FlightOffer


class PersistentFlightCache:
    _file_path = Path("flight_cache.json")
    _ttl = 24 * 3600  # 24h

    @classmethod
    def get(cls, key):
        if not cls._file_path.exists():
            return None

        with open(cls._file_path, "r") as f:
            data = json.load(f)

        entry = data.get(key)
        if not entry:
            return None

        value_dict, timestamp = entry

        if time.time() - timestamp > cls._ttl:
            data.pop(key)
            cls._save(data)
            return None

        return FlightOffer(
            price=value_dict["price"],
            booking_link=value_dict["booking_link"],
        )

    @classmethod
    def set(cls, key, value: FlightOffer):
        data = {}

        if cls._file_path.exists():
            with open(cls._file_path, "r") as f:
                data = json.load(f)

        serialized_value = {
            "price": value.price,
            "booking_link": value.booking_link,
        }

        data[key] = [serialized_value, time.time()]
        cls._save(data)

    @classmethod
    def _save(cls, data):
        with open(cls._file_path, "w") as f:
            json.dump(data, f, indent=2)
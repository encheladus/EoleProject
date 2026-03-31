import pytest
from infrastructure.cache.ram_flight_cache import RamFlightCache


@pytest.fixture(autouse=True)
def clear_cache():
    RamFlightCache._cache = {}


def test_set_and_get():
    RamFlightCache.set("test-key", {"price": 100})
    result = RamFlightCache.get("test-key")
    assert result == {"price": 100}


def test_has_key():
    RamFlightCache.set("another-key", {"price": 200})
    assert RamFlightCache.has("another-key") is True
    assert RamFlightCache.has("non-existent") is False


def test_override_value():
    RamFlightCache.set("override-key", {"price": 300})
    RamFlightCache.set("override-key", {"price": 400})
    assert RamFlightCache.get("override-key") == {"price": 400}

def test_cache_expiration():
    RamFlightCache._ttl = 1
    RamFlightCache.set("key", {"price": 100})

    import time
    time.sleep(2)

    assert RamFlightCache.get("key") is None
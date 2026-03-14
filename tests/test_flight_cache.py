import pytest
from infrastructure.cache.flight_cache import FlightCache  # chemin à adapter

def test_set_and_get():
    FlightCache.set("test-key", {"price": 100})
    result = FlightCache.get("test-key")
    assert result == {"price": 100}

def test_has_key():
    FlightCache.set("another-key", {"price": 200})
    assert FlightCache.has("another-key") is True
    assert FlightCache.has("non-existent") is False

def test_override_value():
    FlightCache.set("override-key", {"price": 300})
    FlightCache.set("override-key", {"price": 400})
    assert FlightCache.get("override-key") == {"price": 400}
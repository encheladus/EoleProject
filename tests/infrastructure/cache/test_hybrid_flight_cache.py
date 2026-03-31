import pytest
import json
import time
from unittest.mock import patch, mock_open
from infrastructure.cache.persistent_flight_cache import PersistentFlightCache
from infrastructure.cache.ram_flight_cache import RamFlightCache
from infrastructure.cache.hybrid_flight_cache import HybridFlightCache

def test_hybrid_cache_reads_from_ram_first():
    RamFlightCache.set("ram-key", {"price": 111})
    # Persistant ne contient rien
    with patch.object(PersistentFlightCache, "get", return_value=None) as mock_persist:
        result = HybridFlightCache.get("ram-key")
        assert result == {"price": 111}
        mock_persist.assert_not_called()

def test_hybrid_cache_reads_from_persistent_if_ram_miss():
    # RAM miss
    RamFlightCache._cache = {}
    with patch.object(PersistentFlightCache, "get", return_value={"price": 222}) as mock_persist:
        result = HybridFlightCache.get("persist-key")
        assert result == {"price": 222}
        # RAM doit maintenant contenir la valeur
        assert RamFlightCache.get("persist-key") == {"price": 222}
        mock_persist.assert_called_once()

def test_hybrid_cache_set_writes_both():
    with patch.object(PersistentFlightCache, "set") as mock_persist:
        HybridFlightCache.set("hybrid-key", {"price": 333})
        # RAM contient la valeur
        assert RamFlightCache.get("hybrid-key") == {"price": 333}
        mock_persist.assert_called_once_with("hybrid-key", {"price": 333})
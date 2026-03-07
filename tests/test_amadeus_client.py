import pytest
from infrastructure.amadeus_client import AmadeusClient
import os

# Normal case → Initialization OK
# Error case → Initialization KO

def test_amadeus_client_initialization_ok(monkeypatch):
    """Connexion OK if keys are available"""
    monkeypatch.setenv("AMADEUS_API_KEY", "fake_key")
    monkeypatch.setenv("AMADEUS_API_SECRET", "fake_secret")

    client_instance = AmadeusClient()
    assert client_instance.get_client() is not None

def test_amadeus_client_initialization_missing_keys(monkeypatch):
    """Connexion OK if keys are unavailable"""
    monkeypatch.delenv("AMADEUS_API_KEY", raising=False)
    monkeypatch.delenv("AMADEUS_API_SECRET", raising=False)

    with pytest.raises(ValueError) as excinfo:
        AmadeusClient()
    assert "The Amadeus API keys are not set in .env" in str(excinfo.value)
import json
import time
from unittest.mock import patch, mock_open
from infrastructure.cache.persistent_flight_cache import PersistentFlightCache

def test_persistent_set_and_get():
    mock_file = mock_open()
    with patch("builtins.open", mock_file), patch("pathlib.Path.exists", return_value=False):
        PersistentFlightCache.set("key1", {"price": 100})
        # Vérifier qu'on a écrit dans le fichier
        mock_file().write.assert_called()

    # Maintenant mock exist pour test get
    data = {"key1": ({"price": 100}, time.time())}
    with patch("builtins.open", mock_open(read_data=json.dumps(data))), \
         patch("pathlib.Path.exists", return_value=True):
        result = PersistentFlightCache.get("key1")
        assert result == {"price": 100}

def test_persistent_expiration():
    timestamp_old = time.time() - (PersistentFlightCache._ttl + 10)
    data = {"key2": ({"price": 200}, timestamp_old)}
    with patch("builtins.open", mock_open(read_data=json.dumps(data))), \
         patch("pathlib.Path.exists", return_value=True), \
         patch("infrastructure.cache.persistent_flight_cache.PersistentFlightCache._save") as mock_save:
        result = PersistentFlightCache.get("key2")
        assert result is None
        # s'assure qu'on a supprimé la clé expirée
        mock_save.assert_called()

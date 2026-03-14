from application.cache_key_builder import build_cache_key


def test_build_flight_cache_key():
    key = build_cache_key(
        origin="CDG",
        destination="ICN",
        departure_date="2026-03-09",
        return_date="2026-03-30"
    )

    assert key == "flight:CDG:ICN:2026-03-09:2026-03-30"
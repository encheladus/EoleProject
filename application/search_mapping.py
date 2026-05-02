from datetime import datetime, timezone


def map_search(origin: str, destination: str, stay_duration: int, search_period: int) -> dict:
    return {
        "origin": origin.strip().upper(),
        "destination": destination.strip().upper(),
        "stay_duration": stay_duration,
        "search_period": search_period,
        "created_at": datetime.now(timezone.utc)
    }
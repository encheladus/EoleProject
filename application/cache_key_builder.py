def build_cache_key(origin, destination, departure_date, return_date):
    return f"flight:{origin}:{destination}:{departure_date}:{return_date}"
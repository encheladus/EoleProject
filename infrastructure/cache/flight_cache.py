import time

class FlightCache:

    _cache = {}
    _ttl = 86400  # 24h

    @classmethod
    def get(cls, key):
        entry = cls._cache.get(key)

        if not entry:
            return None

        value, timestamp = entry

        if time.time() - timestamp > cls._ttl:
            del cls._cache[key]
            return None

        return value

    @classmethod
    def set(cls, key, value):
        cls._cache[key] = (value, time.time())

    @classmethod
    def has(cls, key):
        return cls.get(key) is not None
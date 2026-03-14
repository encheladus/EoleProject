class FlightCache:
    _cache = {}

    @classmethod
    def get(cls, key):
        return cls._cache.get(key)

    @classmethod
    def set(cls, key, value):
        cls._cache[key] = value

    @classmethod
    def has(cls, key):
        return key in cls._cache
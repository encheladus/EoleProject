from infrastructure.cache.persistent_flight_cache import PersistentFlightCache
from infrastructure.cache.ram_flight_cache import RamFlightCache


class HybridFlightCache:

    @staticmethod
    def get(key):
        # d'abord RAM
        value = RamFlightCache.get(key)
        if value:
            return value
        # puis persistant
        value = PersistentFlightCache.get(key)
        if value:
            RamFlightCache.set(key, value)  # recharge RAM
        return value

    @staticmethod
    def set(key, value):
        RamFlightCache.set(key, value)
        PersistentFlightCache.set(key, value)

    @staticmethod
    def has(key):
        return HybridFlightCache.get(key) is not None
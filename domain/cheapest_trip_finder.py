
class CheapestTripFinder:

    @staticmethod
    def find_cheapest(trips):
        valid_trips = [trip for trip in trips if trip["price"] is not None]
        if not valid_trips:
            return None
        cheapest_trip = min(valid_trips, key=lambda trip:float(trip["price"]))
        return cheapest_trip
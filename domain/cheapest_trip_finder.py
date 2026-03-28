
class CheapestTripFinder:

    @staticmethod
    def find_cheapest(trips):
        valid_trips = [trip for trip in trips if trip["price"] is not None]
        if not valid_trips:
            return

        cheapest_price = min(float(trip["price"]) for trip in valid_trips)

        cheapest_trips = [
            trip for trip in valid_trips
            if float(trip["price"]) == cheapest_price
        ]
        return cheapest_trips
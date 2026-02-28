from datetime import date, timedelta

class TravelCombinationGenerator:

    def __init__(self, stay_duration_days: int):
        if stay_duration_days <= 0:
            raise ValueError("stay_duration_days must be positive")
        self.stay_duration_days = stay_duration_days

    def generate(self, departure_dates: list[date]) -> list[tuple[date, date]]:
        return [(d, d + timedelta(days=self.stay_duration_days)) for d in departure_dates]
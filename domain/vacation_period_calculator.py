from datetime import date, timedelta


#search_start = 01/01/2026
#stay_duration = 14 jours
#search_period = 90 jours
class VacationPeriodCalculator:
    @staticmethod
    def generate_possible_departures(
        search_start_date: date,
        stay_duration_days: int,
        search_period_days: int
    ) -> list[date]:

        if stay_duration_days <= 0:
            raise ValueError("stay_duration_days must be positive")

        if search_period_days <= 0:
            raise ValueError("search_period_days must be positive")

        search_end_date = search_start_date + timedelta(days=search_period_days)

        departures = []
        current_date = search_start_date

        while current_date + timedelta(days=stay_duration_days) <= search_end_date:
            departures.append(current_date)
            current_date += timedelta(days=1)

        return departures
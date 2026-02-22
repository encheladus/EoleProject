from datetime import date, timedelta

class DateRangeGenerator:
    @staticmethod
    def generate_departure_dates(start_date, end_date):
        if start_date > end_date:
            raise ValueError("start_date cannot be after end_date")
        dates_list = []
        current_date = start_date
        while current_date <= end_date:
            dates_list.append(current_date)
            current_date += timedelta(days=1)
        # Replacing the while loop by a for loop 
        # delta = (end_date - start_date).days
        # return [start_date + timedelta(days=i) for i in range(delta + 1)]
        return dates_list

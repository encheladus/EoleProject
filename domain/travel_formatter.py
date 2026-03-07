from datetime import date

class TravelFormatter:

    @staticmethod
    def format_combinations(combinations, origin, destination):
      formatted = []
      for dep, ret in combinations:
        formatted.append({
          "departure_date": dep.isoformat(),
          "return_date": ret.isoformat(),
          "destination": destination,
          "origin": origin,
          "price": None
        })
      return formatted

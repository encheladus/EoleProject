def format_cheapest_trips(trips: list[dict], average_price: float) -> str:
    if not trips:
        return "No cheapest trips found."

    first_trip = trips[0]
    number_of_trips_found = len(trips)
    trip_price = float(first_trip["price"])
    economy_made = average_price - trip_price

    date_lines = [
        f"- {trip['departure_date']} to {trip['return_date']}"
        for trip in trips
    ]

    return (
        f"From {first_trip['origin']} airport to {first_trip['destination']} airport, "
        f"there are {number_of_trips_found} cheapest round trips.\n"
        f"Price: {trip_price:.2f}€\n"
        f"Average price: {average_price:.2f}€\n"
        f"Savings: {economy_made:.2f}€\n"
        f"You can go on:\n" + "\n".join(date_lines)
    )
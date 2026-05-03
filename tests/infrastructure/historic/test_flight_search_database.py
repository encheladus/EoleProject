from infrastructure.historic.flight_search_database import FlightSearchDatabase

map_search = {
    "origin": "ICN",
    "destination": "CDG",
    "stay_duration": 10,
    "search_period": 30,
    "created_at": "2026-05-01 14:32:10.123456+00:00"
    }

def test_insert_search_success():
    db = FlightSearchDatabase(":memory:")
    cursor = db.connection.cursor()
    db.insert_search(map_search)
    cursor.execute("SELECT * FROM searches")
    table = cursor.fetchone()
    assert table[1] == "ICN"
    assert table[2] == "CDG"
    assert table[3] == 10
    assert table[4] == 30
    assert table[5] == "2026-05-01 14:32:10.123456+00:00"

trips = {
    "departure_date": "2026-10-09",
    "return_date": "2026-10-29",
    "price": 1200,
    "booking_link": "https://www.google.com",
}
def test_insert_result_success():
    db = FlightSearchDatabase(":memory:")
    cursor = db.connection.cursor()
    search_id = db.insert_search(map_search)
    db.insert_result(trips, search_id, "SERP API")
    cursor.execute("SELECT * FROM flight_offer_snapshot")
    table = cursor.fetchone()
    assert table[1] == search_id
    assert table[2] == "2026-10-09"
    assert table[3] == "2026-10-29"
    assert table[4] == 1200
    assert table[5] == "https://www.google.com"
    assert table[6] == "SERP API"
    assert table[7] is not None
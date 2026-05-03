import sqlite3
from datetime import datetime, timezone

class FlightSearchDatabase:
    def __init__(self, db_path = "eole.db"):
        self.connection = sqlite3.connect(db_path)

        self.connection.execute("PRAGMA foreign_keys = ON")

        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS searches
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                stay_duration INTEGER NOT NULL,
                search_period INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flight_offer_snapshot
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_id INTEGER NOT NULL,
                departure_date TEXT NOT NULL,
                return_date TEXT NOT NULL,
                price REAL,
                booking_link TEXT,
                provider TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (search_id) REFERENCES searches(id) ON DELETE CASCADE
            )
        """)

        self.connection.commit()

    def insert_search(self, map_search: dict):
        search = (map_search["origin"], map_search["destination"], map_search["stay_duration"], map_search["search_period"], map_search["created_at"])
        cursor = self.connection.cursor()
        cursor.execute("""
                    INSERT INTO searches(origin, destination, stay_duration, search_period, created_at)
                    VALUES (?, ?, ?, ?, ?);
                    """, search)
        self.connection.commit()
        return cursor.lastrowid


    def insert_result(self, trips: dict, search_id: int, provider: str):
        trip_result = (trips["departure_date"], trips["return_date"], trips["price"], trips["booking_link"], provider, datetime.now(timezone.utc).isoformat(), search_id)
        cursor = self.connection.cursor()
        cursor.execute("""
                    INSERT INTO flight_offer_snapshot(departure_date, 
                                                      return_date, price, booking_link, 
                                                      provider, created_at, search_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """, trip_result)
        self.connection.commit()
        return cursor.lastrowid
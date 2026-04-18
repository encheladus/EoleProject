import sqlite3

class FlightSearchDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("eole.db")

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
                created_at INTEGER NOT NULL
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
                created_at INTEGER NOT NULL,
                FOREIGN KEY (search_id) REFERENCES searches(id) ON DELETE CASCADE
            )
        """)

        self.connection.commit()

    def insert_offer(self, offer):
        pass
    def  read_offers(self):
        pass
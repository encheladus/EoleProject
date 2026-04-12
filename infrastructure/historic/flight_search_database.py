import sqlite3

class FlightSearchDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("eole.db")
    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS flight_offer()")
    def insert_offer(self, offer):
        pass
    def  read_offers(self):
        pass
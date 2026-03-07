import os
from dotenv import load_dotenv
from amadeus import Client

class AmadeusClient:

    def __init__(self):
        load_dotenv()

        self.client = Client(
            client_id=os.getenv("AMADEUS_API_KEY"),
            client_secret=os.getenv("AMADEUS_API_SECRET")
        )

    def get_client(self):
        return self.client


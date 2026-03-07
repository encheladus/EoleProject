import os
from amadeus import Client

class AmadeusClient:

    def __init__(self):
        api_key = os.getenv("AMADEUS_API_KEY")
        api_secret = os.getenv("AMADEUS_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("The Amadeus API keys are not set in .env")

        self.client = Client(
            client_id=api_key,
            client_secret=api_secret
        )

    def get_client(self):
        return self.client

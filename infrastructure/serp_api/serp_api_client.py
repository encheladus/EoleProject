import os


class SerpApiClient:
    def __init__(self):
        api_key = os.getenv("SERPAPI_API_KEY")

        if not api_key:
            raise ValueError("SERPAPI_API_KEY is not set in the environment")

        self.api_key = api_key

    def get_client(self):
        return self.api_key
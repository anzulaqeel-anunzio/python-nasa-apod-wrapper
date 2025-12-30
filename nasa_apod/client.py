# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests
from datetime import date

class ApodClient:
    BASE_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key: str = "DEMO_KEY"):
        """
        Initialize the APOD client.
        :param api_key: Your NASA API Key. Defaults to 'DEMO_KEY'.
        """
        self.api_key = api_key

    def _make_request(self, params: dict):
        params["api_key"] = self.api_key
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_today(self):
        """Fetch today's APOD."""
        return self._make_request(params={})

    def get_by_date(self, date_obj: date):
        """Fetch APOD for a specific date."""
        return self._make_request(params={"date": date_obj.isoformat()})

    def get_random(self, count: int = 1):
        """Fetch random APOD(s)."""
        return self._make_request(params={"count": count})
    
    def get_range(self, start_date: date, end_date: date):
        """Fetch APODs within a date range."""
        return self._make_request(params={
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        })

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

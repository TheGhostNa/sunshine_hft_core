import time

import requests

from config.alpaca_keys import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, DATA_URL


class AlpacaClient:
    def __init__(self):
        self.api_key = ALPACA_API_KEY
        self.secret_key = ALPACA_SECRET_KEY
        self.base_url = BASE_URL
        self.data_url = DATA_URL
        self.session = requests.Session()
        self.session.headers.update(
            {"APCA-API-KEY-ID": self.api_key, "APCA-API-SECRET-KEY": self.secret_key}
        )

    def get_minute_bars(self, symbol, start, end, limit=1000, retry=3, backoff=1.0):
        url = f"{self.data_url}/v2/stocks/{symbol}/bars"
        params = {"start": start, "end": end, "timeframe": "1Min", "limit": limit}
        for attempt in range(retry):
            try:
                resp = self.session.get(url, params=params)
                resp.raise_for_status()
                data = resp.json()
                return data["bars"]
            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error fetching data: {e}, attempt {attempt + 1} of {retry}")
                time.sleep(backoff * (attempt + 1))
            except Exception as e:
                print(f"Error fetching data: {e}, attempt {attempt + 1} of {retry}")
                time.sleep(backoff * (attempt + 1))
        raise Exception("Max retries exceeded for Alpaca data fetch")

# data_feed/alpaca_realtime.py
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests


class AlpacaRealtimeData:
    def __init__(self, api_key, secret_key, data_url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.data_url = data_url
        self.headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key,
        }

    def get_minute_bars(self, symbol, limit=100):
        """
        Fetch last 'limit' 1-minute bars for symbol.
        """
        end = datetime.now(timezone.utc)
        start = end - timedelta(minutes=limit)

        url = f"{self.data_url}/v2/stocks/{symbol}/bars"
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "timeframe": "1Min",
            "limit": limit,
        }

        resp = requests.get(url, headers=self.headers, params=params)
        resp.raise_for_status()
        data = resp.json()

        if "bars" not in data:
            raise ValueError(f"No bars data returned for {symbol}")

        bars = data["bars"]
        df = pd.DataFrame(bars)
        if df.empty:
            raise ValueError(f"No data fetched for {symbol}")

        # Convert timestamp to datetime and set index
        df["t"] = pd.to_datetime(df["t"])
        df.set_index("t", inplace=True)
        df.rename(
            columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"},
            inplace=True,
        )
        df = df[["open", "high", "low", "close", "volume"]]

        return df

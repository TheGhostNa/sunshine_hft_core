# realtime_trading/data_fetcher.py

import os

from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = REST(API_KEY, API_SECRET, BASE_URL)


def fetch_latest_data(symbol, limit=100):
    try:
        bars = api.get_bars(symbol, TimeFrame.Minute, limit=limit).df

        if bars.empty:
            print(f"❌ No bars returned for {symbol}")
            return None

        df = bars.reset_index()
        print(f"📈 Fetching data for {symbol}")
        return {"symbol": symbol, "df": df}

    except Exception as e:
        print(f"❌ Failed to fetch data for {symbol}: {e}")
        return None

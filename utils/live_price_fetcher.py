# utils/live_price_fetcher.py

import os

from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
API_BASE_URL = os.getenv("APCA_API_BASE_URL")

if not all([API_KEY, API_SECRET, API_BASE_URL]):
    print("❌ ERROR: Missing API credentials in .env!")

api = REST(API_KEY, API_SECRET, API_BASE_URL)


def get_data(symbol, lookback_days=5):
    try:
        symbol = symbol.upper()
        bars = api.get_bars(symbol, TimeFrame.Minute, limit=300).df

        if bars.empty or len(bars) < 30:
            raise ValueError(f"Not enough data for {symbol}")

        bars = bars[["close", "high", "low", "volume"]]
        return bars

    except Exception as e:
        print(f"⚠️ Alpaca fetch failed for {symbol}: {e}")
        return None

import os
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

from .alpaca_api import fetch_data_from_alpaca


def get_latest_close_prices(symbol, limit=50):
    try:
        print(f"🔍 Trying Alpaca API for {limit} prices...")
        alpaca_prices = fetch_data_from_alpaca(symbol, limit=limit)
        if alpaca_prices:
            return alpaca_prices
        raise ValueError("Alpaca fetch failed.")
    except Exception as e:
        print(f"❌ Alpaca fetch failed: {e}")

    try:
        print(f"🔍 Fetching {limit} close prices for {symbol} from Yahoo Finance...")
        end = datetime.now()
        start = end - timedelta(days=limit * 2)
        df = yf.download(symbol, start=start, end=end)
        prices = df["Close"].values[-limit:]  # ✅ Fixed from .tolist()
        print(f"Fetched {len(prices)} close prices for {symbol}. Last price: {prices[-1]}")
        return prices
    except Exception as e:
        print(f"❌ Yahoo Finance fetch failed: {e}")

    try:
        print("🔁 Trying fallback local CSV...")
        fallback_path = os.path.join("data", "sample_data.csv")
        df = pd.read_csv(fallback_path)
        prices = df["Close"].values[-limit:]
        if len(prices) < limit:
            raise ValueError("Not enough fallback data.")
        print(f"✅ Loaded {len(prices)} prices from fallback CSV.")
        return prices
    except Exception as e:
        print(f"❌ CSV fallback failed: {e}")
        raise RuntimeError("Price fetch failed or insufficient data.")

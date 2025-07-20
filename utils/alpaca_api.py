from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

API_KEY = "CK508HHELBVVTEPOL24P"
API_SECRET = "KNbzOQu1rSfLKRUpTVp8kcwSB6MRGfEJermza9PE"

client = StockHistoricalDataClient(API_KEY, API_SECRET)


def fetch_data(symbol):
    print(f"🔍 Fetching data for {symbol} using Alpaca timeframe=1Min...")
    end = datetime.utcnow()
    start = end - timedelta(days=5)

    try:
        request_params = StockBarsRequest(
            symbol_or_symbols=symbol, timeframe=TimeFrame.Minute, start=start, end=end
        )
        bars = client.get_stock_bars(request_params).df
        if symbol in bars.index.names:
            bars = bars.xs(symbol)
        close_prices = bars["close"].tolist()
        last_price = close_prices[-1]
        return close_prices, last_price
    except Exception as e:
        print(f"❌ Alpaca data fetch failed: {e}")

    print("🔁 Switching to Yahoo Finance...")
    try:
        df = yf.download(symbol, period="7d", interval="1m", progress=False)
        if df.empty or "Close" not in df.columns:
            raise ValueError("Yahoo Finance returned no data or missing 'Close' column")
        close_prices = df["Close"].tolist()
        last_price = close_prices[-1]
        return close_prices, last_price
    except Exception as e:
        print(f"❌ Fallback Yahoo Finance fetch failed: {e}")

    print("🔁 Both APIs failed, trying local CSV...")
    try:
        df = pd.read_csv("sample_data.csv")
        close_prices = df["close"].tolist()
        last_price = close_prices[-1]
        print("✅ Loaded fallback sample data.")
        return close_prices, last_price
    except Exception as e:
        print(f"❌ Error fetching data from local CSV: {e}")
        raise ValueError(f"No sufficient data for {symbol}")

# market/live_price_fetcher.py

import yfinance as yf

def fetch_live_price(symbol="AAPL"):
    try:
        data = yf.download(tickers=symbol, period="1d", interval="1m")
        return data
    except Exception as e:
        print(f"Live price fetch failed: {e}")
        return None

import os
from datetime import datetime, timedelta

from alpaca_trade_api.rest import REST
from dotenv import load_dotenv

load_dotenv()


def get_alpaca_api():
    mode = os.getenv("MODE", "paper").lower()
    if mode == "live":
        key = os.getenv("LIVE_API_KEY")
        secret = os.getenv("LIVE_API_SECRET")
        url = os.getenv("LIVE_API_BASE_URL")
    else:
        key = os.getenv("PAPER_API_KEY")
        secret = os.getenv("PAPER_API_SECRET")
        url = os.getenv("PAPER_API_BASE_URL")

    if not all([key, secret, url]):
        raise ValueError("Alpaca API credentials not found in environment variables.")

    return REST(key, secret, url, api_version="v2")


def fetch_data_from_alpaca(symbol: str, limit=50):
    api = get_alpaca_api()
    end_time = datetime.now()
    start_time = end_time - timedelta(days=limit * 2)

    try:
        bars = api.get_bars(
            symbol,
            timeframe="1Day",
            start=start_time.strftime("%Y-%m-%d"),
            end=end_time.strftime("%Y-%m-%d"),
            adjustment="raw",
        ).df

        if symbol not in bars.columns and "close" in bars:
            close_prices = bars["close"].dropna().values[-limit:]
        else:
            bars = bars[bars["symbol"] == symbol]
            close_prices = bars["close"].dropna().values[-limit:]

        return close_prices.tolist()
    except Exception as e:
        raise RuntimeError(f"Alpaca data fetch failed: {e}")

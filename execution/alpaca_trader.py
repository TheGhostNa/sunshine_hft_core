# execution/alpaca_trader.py

import requests

from config.alpaca_keys import ALPACA_API_KEY, ALPACA_SECRET_KEY

BASE_URL = "https://paper-api.alpaca.markets"  # use for paper trading

HEADERS = {"APCA-API-KEY-ID": ALPACA_API_KEY, "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY}


def place_order(symbol, qty, side, order_type="market", time_in_force="gtc"):
    url = f"{BASE_URL}/v2/orders"
    payload = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": order_type,
        "time_in_force": time_in_force,
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        print(f"✅ {side.upper()} order placed for {qty} shares of {symbol}")
    else:
        print("❌ Order failed:", response.json())

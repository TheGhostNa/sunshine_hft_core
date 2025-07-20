# broker/alpaca_connector.py
import os

import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")


def get_account_info():
    account = api.get_account()
    return {
        "equity": account.equity,
        "cash": account.cash,
        "status": account.status,
        "buying_power": account.buying_power,
    }


def submit_order(symbol, qty, side, type="market", time_in_force="gtc"):
    try:
        api.submit_order(symbol=symbol, qty=qty, side=side, type=type, time_in_force=time_in_force)
        print(f"✅ Order submitted: {side.upper()} {qty} {symbol}")
    except Exception as e:
        print(f"❌ Order failed: {e}")

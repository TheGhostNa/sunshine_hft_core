import os

import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

from utils.logger import log_error

load_dotenv()

MODE = os.getenv("MODE", "paper").lower()
API_KEY = os.getenv("PAPER_API_KEY") if MODE == "paper" else os.getenv("LIVE_API_KEY")
API_SECRET = os.getenv("PAPER_API_SECRET") if MODE == "paper" else os.getenv("LIVE_API_SECRET")
BASE_URL = os.getenv("PAPER_API_BASE_URL") if MODE == "paper" else os.getenv("LIVE_API_BASE_URL")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)


def execute_trade(ticker, price, signal, state):
    try:
        qty = 1  # You can replace this with dynamic position sizing logic

        if signal == "BUY" and not state.holding:
            api.submit_order(symbol=ticker, qty=qty, side="buy", type="market", time_in_force="gtc")
            state.holding = True
            return f"✅ Executed BUY {qty} {ticker} @ {price:.2f}"

        elif signal == "SELL" and state.holding:
            api.submit_order(
                symbol=ticker, qty=qty, side="sell", type="market", time_in_force="gtc"
            )
            state.holding = False
            return f"✅ Executed SELL {qty} {ticker} @ {price:.2f}"

    except Exception as e:
        log_error(f"❌ Trade execution failed: {e}")
    return None

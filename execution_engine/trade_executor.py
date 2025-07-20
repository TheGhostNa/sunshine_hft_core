# execution_engine/trade_executor.py

import os

MODE = os.getenv("MODE", "paper").lower()


def execute_trade(signal, symbol, quantity=1):
    print(f"🚀 Executing {signal} trade for {symbol} | Qty: {quantity} | Mode: {MODE}")

    # For now, just simulate it
    if MODE == "live":
        print("⚠️ LIVE mode not enabled yet.")
    else:
        print(f"✅ Paper Trade Executed: {signal} {quantity} shares of {symbol}")

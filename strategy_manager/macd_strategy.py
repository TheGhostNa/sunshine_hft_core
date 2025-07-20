import numpy as np
import talib


def macd_decision(close_prices):
    close_prices = np.array(close_prices, dtype="float64")  # ✅ FIX: ensure NumPy array

    macd, signal, hist = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

    if macd[-1] > signal[-1]:
        return "BUY"
    elif macd[-1] < signal[-1]:
        return "SELL"
    else:
        return "HOLD"

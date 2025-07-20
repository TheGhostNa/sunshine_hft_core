import numpy as np
import talib


def generate_rsi_signal(prices):
    if len(prices) < 14:
        return "hold"
    prices_array = np.array(prices, dtype=float)
    rsi_values = talib.RSI(prices_array, timeperiod=14)
    if rsi_values[-1] < 30:
        return "buy"
    elif rsi_values[-1] > 70:
        return "sell"
    return "hold"

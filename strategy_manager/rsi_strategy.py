import numpy as np
import talib


def rsi_decision(close_prices, rsi_period=14, buy_threshold=52, sell_threshold=60):
    if len(close_prices) < rsi_period:
        print("Not enough data for RSI calculation.")
        return "HOLD"

    np_close = np.array(close_prices)
    rsi_values = talib.RSI(np_close, timeperiod=rsi_period)
    latest_rsi = rsi_values[-1]

    print(f"📊 RSI Value: {latest_rsi:.2f}")

    if latest_rsi < buy_threshold:
        return "BUY"
    elif latest_rsi > sell_threshold:
        return "SELL"
    else:
        return "HOLD"

import numpy as np
import talib


def bollinger_decision(close_prices):
    upper, middle, lower = talib.BBANDS(np.array(close_prices), timeperiod=20, nbdevup=2, nbdevdn=2)
    last_close = close_prices[-1]
    if last_close > upper[-1]:
        return "SELL"
    elif last_close < lower[-1]:
        return "BUY"
    else:
        return "HOLD"

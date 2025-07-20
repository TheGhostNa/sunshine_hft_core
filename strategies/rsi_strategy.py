import pandas as pd
import talib


def generate_rsi_signal(data: pd.DataFrame):
    print("📊 RSI input preview:", data.tail(3))

    close_prices = data["close"]
    rsi = talib.RSI(close_prices, timeperiod=14)

    if rsi.iloc[-1] > 70:
        return "sell"
    elif rsi.iloc[-1] < 30:
        return "buy"
    else:
        return "hold"

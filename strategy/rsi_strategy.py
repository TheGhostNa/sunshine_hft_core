import talib


def rsi_signal(df, period=14):
    close = df["close"].values

    if len(close) < period:
        return "hold"

    rsi = talib.RSI(close, timeperiod=period)

    if rsi[-1] < 30:
        return "buy"
    elif rsi[-1] > 70:
        return "sell"
    else:
        return "hold"

import talib


def macd_bb_signal(df):
    close = df["close"].values

    if len(close) < 35:
        return "hold"

    macd, signal, _ = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    upper, middle, lower = talib.BBANDS(close, timeperiod=20)

    latest_close = close[-1]
    latest_macd = macd[-1]
    latest_signal = signal[-1]
    latest_upper = upper[-1]
    latest_lower = lower[-1]

    if latest_macd > latest_signal and latest_close < latest_lower:
        return "buy"
    elif latest_macd < latest_signal and latest_close > latest_upper:
        return "sell"
    else:
        return "hold"

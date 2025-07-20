import talib


def generate_macd_bb_signal(df):
    close = df["Close"]
    macd, signal, hist = talib.MACD(close)
    upper, middle, lower = talib.BBANDS(close)

    if macd.iloc[-1] > signal.iloc[-1] and close.iloc[-1] < lower.iloc[-1]:
        return "BUY"
    elif macd.iloc[-1] < signal.iloc[-1] and close.iloc[-1] > upper.iloc[-1]:
        return "SELL"
    else:
        return "HOLD"


__all__ = ["generate_macd_bb_signal"]

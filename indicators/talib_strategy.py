import talib


def calculate_indicators(df):
    close = df["close"].values.astype(float)

    df["rsi"] = talib.RSI(close, timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    df["macd"] = macd
    df["macd_signal"] = macd_signal
    df["macd_hist"] = macd_hist

    return df


def should_buy(df):
    latest = df.iloc[-1]
    return latest["rsi"] < 30 and latest["macd"] > latest["macd_signal"]


def should_sell(df):
    latest = df.iloc[-1]
    return latest["rsi"] > 70 or latest["macd"] < latest["macd_signal"]

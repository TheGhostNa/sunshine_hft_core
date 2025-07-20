import pandas as pd
import talib


def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df["rsi"] = talib.RSI(df["close"], timeperiod=14)
    df["macd"], df["macd_signal"], _ = talib.MACD(df["close"])
    df["sma50"] = talib.SMA(df["close"], timeperiod=50)
    df["sma200"] = talib.SMA(df["close"], timeperiod=200)
    return df

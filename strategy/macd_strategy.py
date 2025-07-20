import numpy as np
import talib


def macd_strategy(df):
    """
    Simple MACD strategy:
    - BUY when MACD crosses above Signal
    - SELL when MACD crosses below Signal
    - HOLD otherwise
    """
    if df is None or df.empty or len(df) < 35:
        raise ValueError("Not enough data for MACD strategy.")

    close = df["close"].astype(float).values

    macd, signal, _ = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

    if np.isnan(macd[-1]) or np.isnan(signal[-1]):
        raise ValueError("NaN values in MACD or Signal")

    # Decision logic
    if macd[-1] > signal[-1] and macd[-2] <= signal[-2]:
        return "BUY"
    elif macd[-1] < signal[-1] and macd[-2] >= signal[-2]:
        return "SELL"
    else:
        return "HOLD"

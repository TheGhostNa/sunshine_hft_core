import pandas as pd


def compute_rsi(data: pd.Series, window=14) -> pd.Series:
    delta = data.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def generate_rsi_signals(data: pd.DataFrame, rsi_period=14, rsi_buy=30, rsi_sell=70) -> pd.Series:
    rsi = compute_rsi(data["close"], window=rsi_period)
    signals = pd.Series(0, index=data.index)

    signals[rsi < rsi_buy] = 1  # buy signal
    signals[rsi > rsi_sell] = -1  # sell signal

    return signals.fillna(0)

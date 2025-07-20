import yfinance as yf


def fetch_ohlcv_data(symbol, interval="1d", lookback_days=100):
    df = yf.download(symbol, period=f"{lookback_days}d", interval=interval, progress=False)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df.columns = [col.lower() for col in df.columns]
    df = df.dropna()
    return df

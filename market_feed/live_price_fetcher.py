import yfinance as yf


def get_stock_data(symbol):
    """
    Fetch historical stock data (1m interval, last 5 days) using yfinance.
    Returns pandas DataFrame or None if no data.
    """
    try:
        df = yf.download(
            tickers=symbol, period="5d", interval="1m", progress=False, auto_adjust=True
        )
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"⚠️ YFinance failed for {symbol}: {e}")
        return None


def get_crypto_data(symbol):
    """
    Fetch historical crypto data (1m interval, last 5 days) using yfinance.
    Returns pandas DataFrame or None if no data.
    Note: symbol should be 'bitcoin', 'ethereum', etc.
    """
    try:
        ticker = symbol + "-USD"
        df = yf.download(
            tickers=ticker, period="5d", interval="1m", progress=False, auto_adjust=True
        )
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"⚠️ YFinance failed for {symbol}: {e}")
        return None

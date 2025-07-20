import talib


def calculate_rsi(close_series, period=14):
    return talib.RSI(close_series, timeperiod=period)


def generate_rsi_signal(df, symbol):
    print(f"📊 RSI input preview for {symbol}: {df.tail(3)}")
    if df is None or df.empty or "close" not in df:
        print(f"⚠️ Insufficient data to generate RSI signal for {symbol}")
        return "hold"

    rsi_series = calculate_rsi(df["close"])
    if rsi_series is None or rsi_series.isna().all():
        print(f"⚠️ RSI calculation failed for {symbol}")
        return "hold"

    latest_rsi = rsi_series.iloc[-1]
    print(f"📊 Latest RSI for {symbol}: {latest_rsi:.2f}")

    if latest_rsi < 30:
        return "buy"
    elif latest_rsi > 70:
        return "sell"
    else:
        return "hold"

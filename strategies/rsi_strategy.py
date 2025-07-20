import talib
import pandas as pd

def generate_rsi_signal(df: pd.DataFrame, period: int = 14) -> str:
    print("\n🧪 Starting RSI Signal Generation...")
    print(f"📊 Incoming DataFrame columns: {df.columns.tolist()}")
    print(f"🔢 Total rows: {len(df)}")

    # Step 1: Flatten multi-index if present
    if isinstance(df.columns, pd.MultiIndex):
        if ('close', 'AAPL') in df.columns:
            close_series = df[('close', 'AAPL')]
        else:
            raise ValueError("❌ Column ('close', 'AAPL') not found.")
    else:
        if 'close' in df.columns:
            close_series = df['close']
        else:
            raise ValueError("❌ Column 'close' not found.")

    # Step 2: Prepare close price array
    close_prices = close_series.dropna().values
    print(f"📈 Close price array shape: {close_prices.shape}")
    print(f"📈 Close prices: {close_prices[-5:]}")

    # Step 3: Check if array has enough data
    if len(close_prices) < period:
        raise ValueError(f"❌ Not enough data to compute RSI (required: {period}, got: {len(close_prices)})")

    # Step 4: Compute RSI using TA-Lib
    rsi = talib.RSI(close_prices, timeperiod=period)
    print(f"✅ RSI array shape: {rsi.shape}")
    print(f"✅ Latest RSI values: {rsi[-5:]}")

    latest_rsi = rsi[-1]
    print(f"🔍 Final RSI value: {latest_rsi:.2f}")

    # Step 5: Return signal
    if latest_rsi > 70:
        return "sell"
    elif latest_rsi < 30:
        return "buy"
    else:
        return "hold"

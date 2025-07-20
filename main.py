import yfinance as yf
import pandas as pd
from strategies.rsi_strategy import generate_rsi_signal

def main():
    try:
        symbol = "AAPL"
        print(f"\n📈 Fetching data for: {symbol}")

        # For Sunday/weekend testing, use 1h or 1d interval (1m returns empty on weekends)
        data = yf.download(symbol, period="7d", interval="1h", auto_adjust=False)

        if data.empty:
            raise ValueError("❌ Downloaded data is empty. Market may be closed or symbol invalid.")

        # Rename column to lowercase if needed
        if 'Close' in data.columns:
            data.rename(columns={'Close': 'close'}, inplace=True)

        # Show data shape
        print(f"✅ Data fetched: {len(data)} rows")

        # Generate signal
        signal = generate_rsi_signal(data)
        print(f"📊 RSI Signal: {signal.upper()}")

    except Exception as e:
        print(f"\n⚠️ Error in main(): {e}")

if __name__ == "__main__":
    main()

from strategies.rsi_strategy import generate_rsi_signal
import yfinance as yf

def fetch_price_data(symbol="AAPL", interval="1d", lookback="30d"):
    df = yf.download(symbol, period=lookback, interval=interval)
    if df.empty:
        raise ValueError("No data fetched. Check symbol or network.")
    return df

def main():
    try:
        df = fetch_price_data()
        signal = generate_rsi_signal(df)
        print(f"Current RSI Signal: {signal}")
    except Exception as e:
        print(f"⚠️ Error in main(): {e}")

if __name__ == "__main__":
    main()

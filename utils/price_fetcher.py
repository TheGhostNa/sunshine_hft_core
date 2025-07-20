import pandas as pd
import yfinance as yf


def fetch_price_data(symbol="AAPL", period="1mo", interval="1d"):
    print(f"📈 Fetching data for {symbol}")
    try:
        df = yf.download(
            tickers=symbol,
            period=period,
            interval=interval,
            progress=False,
            group_by="ticker",  # ✅ Ensures proper structure
            auto_adjust=False,  # ✅ We'll handle this manually later
            threads=False,
        )

        # ✅ If grouped, flatten it
        if isinstance(df.columns, pd.MultiIndex):
            df = df[symbol]  # extract the subframe

        df.dropna(inplace=True)

        # ✅ Check again after cleaning
        required_cols = {"Open", "High", "Low", "Close", "Volume"}
        if not required_cols.issubset(df.columns):
            raise Exception(f"❌ Missing required columns: {required_cols - set(df.columns)}")

        # Final check for usable Close series
        if df["Close"].isnull().all() or len(df["Close"]) < 20:
            raise Exception("❌ Invalid Close array")

        return df

    except Exception as e:
        print(f"❌ Price fetch failed: {e}")
        return pd.DataFrame()

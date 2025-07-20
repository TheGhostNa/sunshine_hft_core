from backtesting.backtest_config import END_DATE, START_DATE
from data.historical_price_loader import load_price_data
from strategies.rsi_strategy import (  # You can replace this with macd_bb_signal or combined later
    rsi_signal,
)


def run_backtest(strategy_function, symbol="AAPL"):
    print(f"🔁 Starting backtest for {symbol} using {strategy_function.__name__}...")

    # Load historical price data
    df = load_price_data(symbol, START_DATE, END_DATE)
    if df is None or df.empty:
        print("❌ Failed to load historical data.")
        return

    initial_balance = 100000
    balance = initial_balance
    position = 0  # 0 means no stock, 1 means holding stock
    buy_price = 0

    for i in range(50, len(df)):
        price_slice = df["Close"].iloc[i - 50: i].values.tolist()  # ✅ FIXED LINE
        current_price = df["Close"].iloc[i]

        try:
            signal = strategy_function(price_slice)
        except Exception as e:
            print(f"⚠️ Error during strategy execution: {e}")
            continue

        if signal == "BUY" and position == 0:
            position = 1
            buy_price = current_price
            print(f"📈 BUY at {buy_price} on {df.index[i].date()}")
        elif signal == "SELL" and position == 1:
            profit = current_price - buy_price
            balance += profit
            position = 0
            print(f"📉 SELL at {current_price} on {df.index[i].date()} | Profit: {profit:.2f}")

    if position == 1:
        print(f"📦 Holding stock. Final unrealized value: {df['Close'].iloc[-1]}")

    print(f"\n💰 Final Balance: {balance:.2f}")
    print(f"📊 Net PnL: {balance - initial_balance:.2f}")
    print("✅ Backtest Complete.")


if __name__ == "__main__":
    run_backtest(strategy_function=rsi_signal, symbol="AAPL")

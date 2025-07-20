def simple_backtest(df):
    df = df.copy()
    position = None
    entry_price = 0
    pnl = 0
    trades = 0
    wins = 0

    for i, row in df.iterrows():
        if row["signal"] == "BUY" and position is None:
            position = "LONG"
            entry_price = row["Close"]
        elif row["signal"] == "SELL" and position == "LONG":
            trades += 1
            exit_price = row["Close"]
            trade_pnl = exit_price - entry_price
            if trade_pnl > 0:
                wins += 1
            pnl += trade_pnl
            position = None

    winrate = (wins / trades) * 100 if trades > 0 else 0
    print(f"📊 Backtest: Trades={trades}, Win%={winrate:.2f}, Total PnL={pnl:.2f}")
    return {"total_trades": trades, "winrate": winrate, "total_pnl": pnl}

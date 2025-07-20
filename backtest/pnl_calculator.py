def calculate_pnl(trades, starting_balance=10000):
    balance = starting_balance
    position = None
    entry_price = 0.0
    trade_history = []

    for trade in trades:
        if trade["type"] == "buy" and position is None:
            position = "long"
            entry_price = trade["price"]
            trade_history.append(f"BUY @ {entry_price}")
        elif trade["type"] == "sell" and position == "long":
            profit = trade["price"] - entry_price
            balance += profit
            trade_history.append(f"SELL @ {trade['price']} | PnL: {profit:.2f}")
            position = None
            entry_price = 0.0

    return balance, trade_history

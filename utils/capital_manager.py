import os


def get_trade_quantity(price):
    equity = float(os.getenv("EQUITY", 10000))
    max_percent = 0.1  # risk 10% per trade
    capital = equity * max_percent
    qty = max(int(capital // price), 1)
    return qty

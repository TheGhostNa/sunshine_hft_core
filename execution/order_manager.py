# sunshine_hft_core/execution/order_manager.py

import logging

from utils.alpaca_api import get_account, get_positions, place_order

logging.basicConfig(
    filename="logs/trades.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class OrderManager:
    def __init__(self, max_capital, trade_fraction=0.05):
        self.max_capital = max_capital
        self.trade_fraction = trade_fraction

    def get_available_cash(self):
        account = get_account()
        return float(account.cash)

    def calculate_qty(self, price):
        # Calculate how many shares to buy/sell based on fraction of capital
        allocated_capital = self.max_capital * self.trade_fraction
        qty = int(allocated_capital // price)
        return max(qty, 1)

    def execute_trade(self, symbol, side, price):
        qty = self.calculate_qty(price)
        if qty == 0:
            print(f"Insufficient capital to trade {symbol} at price {price}")
            return False

        order = place_order(symbol, qty, side)
        if order:
            logging.info(
                f"{side.upper()} order placed for {qty} shares of {symbol} at approx price {price}"
            )
            print(f"💰 Trade executed: {side.upper()} {qty} {symbol} @ ~{price}")
            return True
        else:
            print("⚠️ Order failed.")
            return False

    def check_open_positions(self):
        positions = get_positions()
        return positions

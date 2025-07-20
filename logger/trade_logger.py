# logger/trade_logger.py

import csv
import os
from datetime import datetime


class TradeLogger:
    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name
        self.filename = (
            f"logs/{strategy_name.lower().replace('+', '').replace(' ', '_')}_trades.csv"
        )

        os.makedirs("logs", exist_ok=True)

        # Create file with headers if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["timestamp", "symbol", "side", "price", "quantity", "profit", "strategy"]
                )

    def log_trade(self, symbol, side, price, quantity, profit):
        timestamp = datetime.utcnow().isoformat()

        with open(self.filename, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, symbol, side, price, quantity, profit, self.strategy_name])

        print(
            f"✅ Logged {side} trade for {symbol} | {quantity} @ {price} | Strategy: {self.strategy_name} | Profit: {profit}"
        )

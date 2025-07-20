# sunshine_hft_core/backtesting/trade_logger.py

import csv
import os


def log_trade(trade, path="trades.csv"):
    file_exists = os.path.exists(path)
    with open(path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=trade.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(trade)

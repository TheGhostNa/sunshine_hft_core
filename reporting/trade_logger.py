import csv
import os
from datetime import datetime


def log_trade(asset, signal, price, mode="paper", file_path="reporting/trade_log.csv"):
    """Append a new trade to the log file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = [timestamp, asset, signal, price, mode]

    header = ["timestamp", "asset", "signal", "price", "mode"]
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(entry)

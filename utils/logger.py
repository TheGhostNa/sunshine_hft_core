# utils/logger.py

import csv
import json
import os
from datetime import datetime

LOG_DIR = "log"
REPORT_DIR = "reports"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


def log_trade(strategy, signal, symbol, price, quantity):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy,
        "signal": signal,
        "symbol": symbol,
        "price": price,
        "quantity": quantity,
    }

    # JSON log
    json_file = os.path.join(LOG_DIR, f"{strategy}_log.json")
    with open(json_file, "a") as jf:
        jf.write(json.dumps(log_entry) + "\n")

    # CSV report
    csv_file = os.path.join(REPORT_DIR, f"{strategy}_trades.csv")
    write_header = not os.path.exists(csv_file)
    with open(csv_file, "a", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=log_entry.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(log_entry)


def log_error(strategy, message):
    error_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy,
        "error": message,
    }
    error_file = os.path.join(LOG_DIR, f"{strategy}_errors.json")
    with open(error_file, "a") as ef:
        ef.write(json.dumps(error_entry) + "\n")

import json
import os
from datetime import datetime

LOG_FOLDER = "performance_logs"
LOG_FILE = os.path.join(LOG_FOLDER, "trades_log.json")


def ensure_log_folder():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)


def log_trade(strategy, symbol, action, price, profit_loss, trade_outcome):
    """
    Log trade details into a JSON file.
    """
    ensure_log_folder()

    trade_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy,
        "symbol": symbol,
        "action": action,
        "price": price,
        "profit_loss": profit_loss,
        "trade_outcome": trade_outcome,
    }

    # Load existing logs
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                trades = json.load(f)
            except json.JSONDecodeError:
                trades = []
    else:
        trades = []

    trades.append(trade_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(trades, f, indent=4)


def read_trade_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

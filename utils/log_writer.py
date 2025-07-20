import csv
import json
import os
from datetime import datetime

LOG_DIR = "logs"


def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def get_log_path(strategy_name, extension):
    ensure_log_dir()
    filename = f"{strategy_name.lower()}_log.{extension}"
    return os.path.join(LOG_DIR, filename)


def write_json_log(strategy_name, data):
    path = get_log_path(strategy_name, "json")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def write_csv_log(strategy_name, data):
    path = get_log_path(strategy_name, "csv")
    if not data:
        return

    keys = data[0].keys()
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def log_strategy(strategy_name, trades):
    timestamped = {
        "strategy": strategy_name,
        "generated_at": datetime.utcnow().isoformat(),
        "trades": trades,
    }
    write_json_log(strategy_name, timestamped)
    write_csv_log(strategy_name, trades)

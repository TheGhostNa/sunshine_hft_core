import os
from datetime import datetime

import pandas as pd


def log_pnl(asset, action, price, quantity, timestamp=None):
    log_path = "reporting/pnl_logs.csv"
    timestamp = timestamp or datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "asset": asset,
        "action": action,
        "price": price,
        "quantity": quantity,
    }
    df = pd.DataFrame([data])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode="a", header=False, index=False)
    else:
        df.to_csv(log_path, index=False)

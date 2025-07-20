# meta_strategy/meta_logger.py

import json
import os
from datetime import datetime


def log_meta_strategy(symbol, signal, meta_info, log_dir="logs/meta"):
    """
    Logs meta-strategy decisions to a timestamped JSON file.
    """
    os.makedirs(log_dir, exist_ok=True)
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "symbol": symbol,
        "signal": signal,
        "meta": meta_info,
    }

    log_file = os.path.join(log_dir, f"{symbol}_meta_log.json")
    with open(log_file, "a") as f:
        f.write(json.dumps(log_data) + "\n")

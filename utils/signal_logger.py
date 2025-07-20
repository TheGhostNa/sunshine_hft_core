# utils/signal_logger.py

import os
from datetime import datetime


def log_signals(symbol, signals_df):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    filename = f"{log_dir}/{symbol}_signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    signals_df.to_csv(filename, index=False)
    print(f"Signals logged to {filename}")

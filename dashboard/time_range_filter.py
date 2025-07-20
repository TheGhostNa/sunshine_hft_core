from datetime import datetime, timedelta

import pandas as pd


def filter_log_by_days(filename, days=7):
    df = pd.read_csv(filename, parse_dates=["timestamp"])
    cutoff = datetime.now() - timedelta(days=days)
    return df[df["timestamp"] >= cutoff]

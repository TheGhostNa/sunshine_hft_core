import csv
import json
import os
from datetime import datetime

import pandas as pd

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)


def log_trade(strategy_name, trade_data):
    log_file = os.path.join(REPORTS_DIR, f"{strategy_name}_log.json")

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(trade_data)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)


def generate_summary(strategy_name):
    log_file = os.path.join(REPORTS_DIR, f"{strategy_name}_log.json")
    summary_file = os.path.join(REPORTS_DIR, f"{strategy_name}_summary.csv")

    if not os.path.exists(log_file):
        print(f"⚠️ No log file found for: {strategy_name}")
        return

    with open(log_file, "r") as f:
        trades = json.load(f)

    df = pd.DataFrame(trades)
    if df.empty:
        print(f"⚠️ No trades recorded for: {strategy_name}")
        return

    total_trades = len(df)
    wins = df[df["profit"] > 0].shape[0]
    losses = df[df["profit"] <= 0].shape[0]
    win_rate = (wins / total_trades) * 100 if total_trades else 0
    total_profit = df["profit"].sum()
    avg_profit = df["profit"].mean()

    summary = {
        "Strategy": strategy_name.upper(),
        "Total Trades": total_trades,
        "Wins": wins,
        "Losses": losses,
        "Win Rate (%)": round(win_rate, 2),
        "Total Profit": round(total_profit, 2),
        "Avg Profit/Trade": round(avg_profit, 2),
        "Last Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Save summary as CSV
    with open(summary_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary.keys())
        writer.writeheader()
        writer.writerow(summary)

    print(f"✅ Summary generated: {summary_file}")

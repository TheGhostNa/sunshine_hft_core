import json
import os

import pandas as pd


def process_log(log_path):
    try:
        with open(log_path, "r") as f:
            data = json.load(f)
        signals = data.get("signals", [])
        rows = []
        for entry in signals:
            rows.append(
                {
                    "symbol": entry.get("symbol", "UNKNOWN"),
                    "signal": entry.get("signal", "HOLD"),
                }
            )
        return rows
    except Exception as e:
        print(f"⚠️ Failed to process {log_path}: {e}")
        return []


def main():
    log_dir = "log"
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    strategies = ["rsi", "macd_bb", "meta_strategy"]
    for strategy in strategies:
        log_file = os.path.join(log_dir, f"{strategy}_strategy_log.json")
        if os.path.exists(log_file):
            print(f"✅ {strategy.upper()} log OK")
            signals = process_log(log_file)
            df = pd.DataFrame(signals)
            df.to_csv(os.path.join(report_dir, f"{strategy}_signals.csv"), index=False)
        else:
            print(f"⚠️ Missing log: {log_file}")


if __name__ == "__main__":
    print("🔁 Running Auto Report...")
    main()

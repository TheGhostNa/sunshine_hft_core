import json
import os


def summarize_log(log_path, strategy_name):
    try:
        with open(log_path, "r") as f:
            data = json.load(f)
        signals = data.get("signals", [])
        buy = sum(1 for s in signals if s.get("signal") == "BUY")
        sell = sum(1 for s in signals if s.get("signal") == "SELL")
        return {"strategy": strategy_name, "total_signals": len(signals), "buy": buy, "sell": sell}
    except Exception as e:
        print(f"⚠️ Error loading {strategy_name}: {e}")
        return None


def main():
    strategies = ["rsi", "macd_bb", "meta_strategy"]
    for strategy in strategies:
        log_file = os.path.join("log", f"{strategy}_strategy_log.json")
        summary = summarize_log(log_file, strategy)
        if summary:
            print(summary)


if __name__ == "__main__":
    main()

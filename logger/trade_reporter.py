import matplotlib.pyplot as plt
import pandas as pd


def generate_trade_summary():
    try:
        df = pd.read_csv("logs/trade_log.csv")
    except FileNotFoundError:
        print("❌ No trade logs found.")
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.sort_values("timestamp", inplace=True)

    # PNL Estimation (Fake for now)
    df["pnl"] = df["price"].diff().fillna(0)
    df["cumulative_pnl"] = df["pnl"].cumsum()

    # Plot PNL over time
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["cumulative_pnl"], marker="o")
    plt.title("Cumulative PnL Over Time")
    plt.xlabel("Time")
    plt.ylabel("PnL (USD)")
    plt.grid()
    plt.tight_layout()
    plt.savefig("logs/summary_report.png")
    print("📈 Summary Report Saved: logs/summary_report.png")

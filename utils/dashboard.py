import pandas as pd

LOG_FILE = "data/performance_log.csv"


def show_summary():
    try:
        df = pd.read_csv(LOG_FILE)
    except FileNotFoundError:
        print("No performance logs found yet.")
        return

    print("\n--- Strategy Performance Summary ---\n")

    # Group by strategy and summarize key metrics
    summary = df.groupby("strategy").agg(
        {
            "profit_loss": ["sum", "mean"],
            "trade_outcome": lambda x: (x == "win").mean(),  # Win rate %
        }
    )

    summary.columns = ["Total PnL", "Average PnL", "Win Rate"]
    summary["Win Rate"] = summary["Win Rate"] * 100  # Convert to %
    print(summary)
    print("\n-----------------------------------\n")

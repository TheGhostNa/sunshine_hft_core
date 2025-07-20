import matplotlib.pyplot as plt
import pandas as pd


def generate_comparison_chart(csv_path, save_path="reports/comparison_chart.png"):
    df = pd.read_csv(csv_path)

    strategies = df["Strategy"]
    df["Total Trades"]
    win_rates = df["Win Rate (%)"]
    avg_profit = df["Avg Profit per Trade"]
    total_profit = df["Total Profit"]

    plt.figure(figsize=(12, 8))

    # Total Profit
    plt.subplot(3, 1, 1)
    plt.bar(strategies, total_profit, color="green")
    plt.title("Total Profit per Strategy")
    plt.ylabel("Total Profit ($)")

    # Win Rate
    plt.subplot(3, 1, 2)
    plt.bar(strategies, win_rates, color="blue")
    plt.title("Win Rate per Strategy")
    plt.ylabel("Win Rate (%)")

    # Average Profit
    plt.subplot(3, 1, 3)
    plt.bar(strategies, avg_profit, color="orange")
    plt.title("Average Profit per Trade")
    plt.ylabel("Profit ($)")

    plt.tight_layout()
    plt.savefig(save_path)
    print(f"📈 Saved chart to {save_path}")

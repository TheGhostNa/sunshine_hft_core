# 📁 Folder: dashboard
# 📄 File: visualize.py

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(style="whitegrid")

LOG_FILE = "logs/trades.csv"


def load_trades():
    if not os.path.exists(LOG_FILE):
        print("❌ No trade logs found at logs/trades.csv")
        return pd.DataFrame()
    return pd.read_csv(LOG_FILE)


def plot_strategy_decisions(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="strategy", hue="decision")
    plt.title("Strategy Decisions Count")
    plt.xlabel("Strategy")
    plt.ylabel("Count")
    plt.legend(title="Decision")
    plt.tight_layout()
    plt.show()


def plot_profit_curve(df):
    df["cumulative_profit"] = df["profit"].cumsum()
    plt.figure(figsize=(12, 5))
    plt.plot(df["timestamp"], df["cumulative_profit"], marker="o")
    plt.title("Cumulative Profit Over Time")
    plt.xlabel("Time")
    plt.ylabel("Cumulative Profit ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_trade_outcomes(df):
    df["outcome"] = df["profit"].apply(lambda x: "Win" if x > 0 else "Loss")
    sns.countplot(data=df, x="outcome", palette="Set2")
    plt.title("Win/Loss Distribution")
    plt.xlabel("Trade Outcome")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def run_dashboard():
    df = load_trades()
    if df.empty:
        return
    print("📊 Generating Dashboard...\n")
    plot_strategy_decisions(df)
    plot_profit_curve(df)
    plot_trade_outcomes(df)


if __name__ == "__main__":
    run_dashboard()

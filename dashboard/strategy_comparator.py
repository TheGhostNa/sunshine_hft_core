import matplotlib.pyplot as plt
import pandas as pd


def compare_strategies():
    files = ["logs/rsi_trades.csv", "logs/macd_trades.csv", "logs/meta_trades.csv"]
    names = ["RSI", "MACD+BB", "Meta"]

    pnl_data = []
    for file, name in zip(files, names):
        try:
            df = pd.read_csv(file)
            pnl_data.append((name, df["profit"].sum()))
        except BaseException:
            pnl_data.append((name, 0))

    names, profits = zip(*pnl_data)
    plt.bar(names, profits)
    plt.title("Strategy Profit Comparison")
    plt.ylabel("Total Profit")
    plt.savefig("strategy_comparison.png")
    plt.close()

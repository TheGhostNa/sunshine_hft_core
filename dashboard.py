import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter


class StrategyDashboard:
    def __init__(self, rsi_log="rsi_trades.csv", macd_log="macd_trades.csv"):
        self.rsi_df = self._load_data(rsi_log)
        self.macd_df = self._load_data(macd_log)

    def _load_data(self, filename):
        df = pd.read_csv(filename, parse_dates=["timestamp"])
        df["cumulative_pnl"] = df["profit"].cumsum()
        df["drawdown"] = df["cumulative_pnl"] - df["cumulative_pnl"].cummax()
        return df

    def generate_report(self):
        # Calculate metrics
        rsi_metrics = self._calculate_metrics(self.rsi_df)
        macd_metrics = self._calculate_metrics(self.macd_df)

        # Plot comparison
        self._plot_pnl_comparison()
        self._plot_drawdown()

        return pd.DataFrame([rsi_metrics, macd_metrics], index=["RSI", "MACD+BB"])

    def _calculate_metrics(self, df):
        wins = df[df["profit"] > 0]
        losses = df[df["profit"] < 0]

        return {
            "Total PnL": df["profit"].sum(),
            "Sharpe Ratio": df["profit"].mean() / df["profit"].std(),
            "Max Drawdown": df["drawdown"].min(),
            "Win Rate": len(wins) / len(df),
            "Avg Win": wins["profit"].mean(),
            "Avg Loss": losses["profit"].mean(),
            "Profit Factor": wins["profit"].sum() / abs(losses["profit"].sum()),
        }

    def _plot_pnl_comparison(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.rsi_df["timestamp"], self.rsi_df["cumulative_pnl"], label="RSI")
        plt.plot(self.macd_df["timestamp"], self.macd_df["cumulative_pnl"], label="MACD+BB")
        plt.title("Strategy PnL Comparison")
        plt.ylabel("Cumulative PnL (USD)")
        plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("pnl_comparison.png")
        plt.close()

    def _plot_drawdown(self):
        plt.figure(figsize=(12, 4))
        plt.fill_between(
            self.rsi_df["timestamp"], self.rsi_df["drawdown"], 0, alpha=0.3, label="RSI"
        )
        plt.fill_between(
            self.macd_df["timestamp"], self.macd_df["drawdown"], 0, alpha=0.3, label="MACD+BB"
        )
        plt.title("Strategy Drawdown")
        plt.ylabel("Drawdown (USD)")
        plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("drawdown_comparison.png")
        plt.close()


# Usage example
if __name__ == "__main__":
    dashboard = StrategyDashboard()
    report = dashboard.generate_report()
    print(report)
    report.to_html("strategy_report.html")

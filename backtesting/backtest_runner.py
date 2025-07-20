# sunshine_hft_core/backtesting/backtest_runner.py

import pandas as pd

from backtesting.backtest_config import (
    END_DATE,
    INITIAL_CAPITAL,
    START_DATE,
    STRATEGY,
    TRADE_FRACTION,
)
from backtesting.metrics import calculate_metrics
from backtesting.trade_logger import log_trade
from strategies.combined_strategy import generate_combined_signal
from strategies.macd_bb_strategy import macd_bb_signal
from strategies.rsi_strategy import rsi_signal


def load_data():
    df = pd.read_csv("data/historical_data.csv", parse_dates=["Date"])
    df = df[(df["Date"] >= START_DATE) & (df["Date"] <= END_DATE)]
    df.reset_index(drop=True, inplace=True)
    return df


def run_backtest():
    data = load_data()
    capital = INITIAL_CAPITAL
    trades = []

    for i in range(30, len(data)):
        prices = data["Close"].iloc[i - 30: i].tolist()

        if STRATEGY == "rsi":
            signal = rsi_signal(prices)
        elif STRATEGY == "macd_bb":
            signal = macd_bb_signal(prices)
        elif STRATEGY == "combined":
            signal = generate_combined_signal(prices)
        else:
            raise ValueError("Invalid strategy in config")

        date = data["Date"].iloc[i]
        price = prices[-1]

        if signal in ["BUY", "SELL"]:
            quantity = (capital * TRADE_FRACTION) / price
            profit = quantity * (price * (1 if signal == "SELL" else -1))
            capital += profit

            trade = {
                "date": date,
                "action": signal,
                "price": price,
                "quantity": quantity,
                "profit": profit,
                "equity": capital,
            }
            log_trade(trade)
            trades.append(trade)

    print("✅ Backtest completed.")
    print("📈 Final Capital:", round(capital, 2))
    print("📊 Metrics:")
    print(calculate_metrics(trades))

# File: backtest/backtest_engine.py

import pandas as pd


class BacktestEngine:
    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.position = 0
        self.position_price = 0
        self.trades = []
        self.equity_curve = []

    def run_backtest(self, data: pd.DataFrame, signals: pd.Series):
        """
        Run backtest on given data with buy/sell signals.
        Args:
            data (pd.DataFrame): price data with 'close' column
            signals (pd.Series): trading signals, e.g., 1 for buy, -1 for sell, 0 for hold
        Returns:
            final equity value, list of executed trades
        """
        for i in range(len(data)):
            signal = signals.iloc[i]
            price = data["close"].iloc[i]

            if signal == 1 and self.cash >= price:
                # Buy one unit
                self.position += 1
                self.cash -= price
                self.position_price = price  # avg price can be refined
                self.trades.append(("BUY", price, i))
            elif signal == -1 and self.position > 0:
                # Sell one unit
                self.position -= 1
                self.cash += price
                self.trades.append(("SELL", price, i))

            # Calculate equity
            equity = self.cash + self.position * price
            self.equity_curve.append(equity)

        final_value = (
            self.cash + self.position * data["close"].iloc[-1] if len(data) > 0 else self.cash
        )
        return final_value, self.trades

    def get_equity_curve(self):
        return self.equity_curve

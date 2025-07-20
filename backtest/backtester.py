# backtest/backtester.py

import pandas as pd
from strategy.strategy_combiner import combined_signal_generator
from execution.order_executor import simulate_order_execution

def run_backtest(data: pd.DataFrame):
    balance = 10000
    position = None

    for index in range(len(data)):
        current_data = data.iloc[:index + 1]
        signal = combined_signal_generator(current_data)

        if signal == 'buy' and position is None:
            position = {'buy_price': data.iloc[index]['Close']}
        elif signal == 'sell' and position:
            profit = data.iloc[index]['Close'] - position['buy_price']
            balance += profit
            position = None

    return balance

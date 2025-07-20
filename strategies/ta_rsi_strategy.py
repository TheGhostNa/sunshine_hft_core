# === File: sunshine_hft_core/strategy/ta_rsi_strategy.py ===
import numpy as np
import talib


def generate_rsi_signals(close_prices, period=14, oversold=35, overbought=65):
    rsi = talib.RSI(close_prices, timeperiod=period)
    buy_signals = []
    sell_signals = []

    for i in range(len(rsi)):
        if np.isnan(rsi[i]):
            buy_signals.append(0)
            sell_signals.append(0)
        elif rsi[i] < oversold:
            buy_signals.append(1)
            sell_signals.append(0)
        elif rsi[i] > overbought:
            buy_signals.append(0)
            sell_signals.append(1)
        else:
            buy_signals.append(0)
            sell_signals.append(0)

    return buy_signals, sell_signals, rsi

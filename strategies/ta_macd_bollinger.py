import numpy as np
import talib


def generate_macd_bollinger_signals(close_prices):
    close_prices = np.asarray(close_prices, dtype=np.float64)

    macd, macdsignal, _ = talib.MACD(close_prices)
    upper, middle, lower = talib.BBANDS(close_prices, timeperiod=20)

    buy_signals = []
    sell_signals = []
    trades = []

    for i in range(len(close_prices)):
        price = close_prices[i]

        if (
            i < 1
            or np.isnan(macd[i])
            or np.isnan(macdsignal[i])
            or np.isnan(lower[i])
            or np.isnan(upper[i])
        ):
            buy_signals.append(None)
            sell_signals.append(None)
            continue

        if macd[i] > macdsignal[i] and price < lower[i]:
            buy_signals.append(price)
            sell_signals.append(None)
            trades.append({"type": "BUY", "price": price, "index": i})

        elif macd[i] < macdsignal[i] and price > upper[i]:
            buy_signals.append(None)
            sell_signals.append(price)
            trades.append({"type": "SELL", "price": price, "index": i})
        else:
            buy_signals.append(None)
            sell_signals.append(None)

    return buy_signals, sell_signals, trades

import numpy as np
import talib


def generate_macd_bollinger_signals(
    close_prices, macd_fast=12, macd_slow=26, macd_signal=9, bb_period=20, bb_stddev=2
):
    buy_signals = []
    sell_signals = []

    macd, macd_signal_line, macd_hist = talib.MACD(
        close_prices, fastperiod=macd_fast, slowperiod=macd_slow, signalperiod=macd_signal
    )
    upperband, middleband, lowerband = talib.BBANDS(
        close_prices, timeperiod=bb_period, nbdevup=bb_stddev, nbdevdn=bb_stddev
    )

    for i in range(len(close_prices)):
        if np.isnan(macd[i]) or np.isnan(macd_signal_line[i]):
            buy_signals.append(0)
            sell_signals.append(0)
            continue

        macd_cross_up = (
            macd[i] > macd_signal_line[i] and macd[i - 1] <= macd_signal_line[i - 1]
            if i > 0
            else False
        )
        macd_cross_down = (
            macd[i] < macd_signal_line[i] and macd[i - 1] >= macd_signal_line[i - 1]
            if i > 0
            else False
        )

        if macd_cross_up:
            buy_signals.append(1)
            sell_signals.append(0)
        elif macd_cross_down:
            buy_signals.append(0)
            sell_signals.append(1)
        else:
            buy_signals.append(0)
            sell_signals.append(0)

    return buy_signals, sell_signals, macd_hist

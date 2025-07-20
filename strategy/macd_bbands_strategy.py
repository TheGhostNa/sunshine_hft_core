import numpy as np
import talib


def get_macd_bb_signal(price_list):
    """
    Combines MACD and Bollinger Bands signals.

    :param price_list: List of historical prices (floats)
    :return: "BUY", "SELL", or "HOLD"
    """
    try:
        close_prices = np.array(price_list, dtype=np.float64)

        # MACD Calculation
        macd, signal, _ = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)
        if macd is None or signal is None or np.isnan(macd[-1]) or np.isnan(signal[-1]):
            return "HOLD"

        macd_diff = macd[-1] - signal[-1]

        # Bollinger Bands Calculation
        upper, middle, lower = talib.BBANDS(
            close_prices, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0
        )

        # Most recent values
        price = close_prices[-1]
        upper_band = upper[-1]
        lower_band = lower[-1]

        print(f"📈 MACD: {macd[-1]:.2f}, Signal: {signal[-1]:.2f}, Diff: {macd_diff:.2f}")
        print(f"📉 BBands → Upper: {upper_band:.2f}, Lower: {lower_band:.2f}, Price: {price:.2f}")

        # Signal Logic
        if macd_diff > 0 and price < lower_band:
            return "BUY"
        elif macd_diff < 0 and price > upper_band:
            return "SELL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error in MACD+BB Strategy: {e}")
        return "HOLD"

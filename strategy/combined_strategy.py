import numpy as np

from strategies.macd_bb_strategy import macd_bb_signal
from strategies.rsi_strategy import rsi_signal


def generate_combined_signal(prices):
    try:
        if not isinstance(prices, (list, np.ndarray)) or len(prices) < 30:
            raise ValueError("Insufficient or invalid price data for combined strategy.")

        prices = np.array(prices)

        rsi_result = rsi_signal(prices)
        macd_result = macd_bb_signal(prices)

        print(f"📊 RSI signal: {rsi_result}")
        print(f"📊 MACD+BB signal: {macd_result}")

        # Simple logic: if both say BUY → buy; both say SELL → sell; otherwise HOLD
        if rsi_result == "BUY" and macd_result == "BUY":
            return "BUY"
        elif rsi_result == "SELL" and macd_result == "SELL":
            return "SELL"
        else:
            return "HOLD"

    except Exception as e:
        print(f"Combined signal error: {e}")
        return "HOLD"

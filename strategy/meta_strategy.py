# strategy/meta_strategy_manager.py

from strategy.macd_bb_strategy import macd_bb_signal
from strategy.rsi_strategy import rsi_signal


class MetaStrategyManager:
    def __init__(self, weights=None):
        """
        Initialize the Meta Strategy Manager with weights for each sub-strategy.
        weights: dictionary like {'rsi': 0.5, 'macd_bb': 0.5}
        """
        self.weights = weights if weights else {"rsi": 0.5, "macd_bb": 0.5}

    def combine_signals(self, df):
        """
        Combine signals from all sub-strategies using a weighted voting system.
        Returns: 'BUY', 'SELL', or 'HOLD'
        """
        try:
            rsi = rsi_signal(df)
        except Exception as e:
            print(f"⚠️ RSI strategy failed: {e}")
            rsi = "HOLD"

        try:
            macd_bb = macd_bb_signal(df)
        except Exception as e:
            print(f"⚠️ MACD+BB strategy failed: {e}")
            macd_bb = "HOLD"

        # Convert signals to numeric scores
        mapping = {"BUY": 1, "HOLD": 0, "SELL": -1}
        rsi_val = mapping.get(rsi, 0)
        macd_val = mapping.get(macd_bb, 0)

        # Weighted combination
        combined_score = self.weights["rsi"] * rsi_val + self.weights["macd_bb"] * macd_val

        # Threshold decision
        if combined_score > 0.2:
            return "BUY"
        elif combined_score < -0.2:
            return "SELL"
        else:
            return "HOLD"

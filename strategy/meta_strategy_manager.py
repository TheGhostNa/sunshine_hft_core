from strategy.macd_bb_strategy import macd_bb_signal
from strategy.rsi_strategy import rsi_signal


class MetaStrategyManager:
    def combine_signals(self, df, asset):
        rsi = rsi_signal(df)
        macd = macd_bb_signal(df)

        if rsi == "buy" or macd == "buy":
            return "buy", "Meta"
        elif rsi == "sell" or macd == "sell":
            return "sell", "Meta"
        else:
            return "hold", "Meta"

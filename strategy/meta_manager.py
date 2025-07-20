class MetaStrategyManager:
    def __init__(self, strategy_weights):
        """
        strategy_weights: dict like {"rsi": 0.6, "macd_bb": 0.4}
        """
        self.strategy_weights = strategy_weights
        self.last_signal_time = {}  # cooldown tracker
        self.cooldown_seconds = 300  # 5 min cooldown

    def weighted_decision(self, signals: dict, symbol: str):
        """
        signals: {"rsi": "buy", "macd_bb": "hold"}
        """
        import time
        from collections import defaultdict

        now = time.time()
        if symbol in self.last_signal_time:
            if now - self.last_signal_time[symbol] < self.cooldown_seconds:
                return "hold"  # still in cooldown

        score = defaultdict(float)
        for strat, signal in signals.items():
            weight = self.strategy_weights.get(strat, 0)
            score[signal] += weight

        # Decision logic
        if score["buy"] > 0.5:
            final = "buy"
        elif score["sell"] > 0.5:
            final = "sell"
        else:
            final = "hold"

        if final != "hold":
            self.last_signal_time[symbol] = now

        return final

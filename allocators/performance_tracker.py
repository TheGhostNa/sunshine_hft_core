class StrategyPerformanceTracker:
    def __init__(self, strategy_names):
        self.strategy_stats = {name: {"pnl": 0.0, "trades": 0} for name in strategy_names}

    def update(self, strategy_name, pnl):
        if strategy_name in self.strategy_stats:
            self.strategy_stats[strategy_name]["pnl"] += pnl
            self.strategy_stats[strategy_name]["trades"] += 1

    def get_scores(self):
        scores = {}
        for name, stats in self.strategy_stats.items():
            trades = stats["trades"]
            if trades > 0:
                scores[name] = stats["pnl"] / trades
            else:
                scores[name] = 0.1  # default base score
        return scores

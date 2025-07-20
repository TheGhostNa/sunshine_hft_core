from .capital_splitter import CapitalSplitter
from .performance_tracker import StrategyPerformanceTracker
from .risk_model import RiskModel


class CapitalAllocator:
    def __init__(self, total_capital, strategy_names):
        self.total_capital = total_capital
        self.strategy_names = strategy_names
        self.performance_tracker = StrategyPerformanceTracker(strategy_names)
        self.risk_model = RiskModel()
        self.capital_splitter = CapitalSplitter()

    def update_performance(self, strategy_name, pnl):
        self.performance_tracker.update(strategy_name, pnl)

    def allocate(self):
        X1, X2 = self.capital_splitter.split(self.total_capital)
        strategy_scores = self.performance_tracker.get_scores()
        strategy_risks = self.risk_model.get_risks(strategy_scores)

        allocation = {}
        total_score = sum([score for score in strategy_scores.values()])

        for strategy in self.strategy_names:
            score = strategy_scores[strategy]
            risk_weight = 1.0 - strategy_risks.get(strategy, 0.5)  # Default 50% risk weight
            proportion = (score / total_score) if total_score > 0 else 1 / len(self.strategy_names)
            allocated_capital = X2 * proportion * risk_weight
            allocation[strategy] = round(allocated_capital, 2)

        return {
            "safe_capital": round(X1, 2),
            "loop_capital": round(X2, 2),
            "strategy_allocation": allocation,
        }

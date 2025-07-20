class RiskModel:
    def get_risks(self, strategy_scores):
        max_score = max(strategy_scores.values()) if strategy_scores else 1.0
        risks = {}
        for name, score in strategy_scores.items():
            # Higher score = lower risk
            risks[name] = 1.0 - (score / max_score) if max_score != 0 else 0.5
        return risks

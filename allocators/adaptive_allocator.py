import pandas as pd


class AdaptiveAllocator:
    def __init__(self, strategy_names):
        self.strategy_names = strategy_names
        self.weights = pd.Series(1 / len(strategy_names), index=strategy_names)

    def update(self, returns_df):
        momentum = returns_df.mean()
        volatility = returns_df.std()
        score = momentum / (volatility + 1e-6)
        new_weights = score.clip(lower=0)
        self.weights = new_weights / new_weights.sum()

    def get_weights(self):
        return self.weights.to_dict()

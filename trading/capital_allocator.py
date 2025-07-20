class CapitalAllocator:
    def __init__(self, total_equity=10000):
        self.total_equity = total_equity
        self.asset_allocation = {}

    def decide(self, asset, signal, strategy_name):
        allocation = self.total_equity / 10  # 10% per trade
        price = 100  # fallback if real price is not fetched (overwrite in execute)
        quantity = allocation // price

        if signal == "buy":
            return "buy", quantity, strategy_name
        elif signal == "sell":
            return "sell", quantity, strategy_name
        else:
            return "hold", 0, strategy_name

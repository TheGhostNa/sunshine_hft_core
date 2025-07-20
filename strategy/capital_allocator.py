class CapitalAllocator:
    def __init__(self, total_equity):
        self.total_equity = total_equity
        self.allocations = {
            "hold": 0.4 * total_equity,
            "trade": 0.5 * total_equity,
            "reinvest": 0.1 * total_equity,
        }
        self.position_memory = {}

    def decide(self, signal, asset_type="stock", symbol=""):
        """
        Decide what to do based on signal and internal allocation.
        """
        if symbol not in self.position_memory:
            self.position_memory[symbol] = {"last_action": "HOLD", "position": 0}

        if signal == "BUY" and self.allocations["trade"] > 0:
            self.position_memory[symbol]["last_action"] = "BUY"
            return "BUY"
        elif signal == "SELL" and self.position_memory[symbol]["position"] > 0:
            self.position_memory[symbol]["last_action"] = "SELL"
            return "SELL"
        else:
            return "HOLD"

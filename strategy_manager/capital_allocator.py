# strategy_manager/capital_allocator.py
from typing import Dict, List


class CapitalAllocator:
    def __init__(
        self, max_trade_pct=0.1, min_trade_pct=0.01, increase_factor=1.1, decrease_factor=0.9
    ):
        """
        Controls adaptive capital allocation per trade.
        """
        self.max_trade_pct = max_trade_pct
        self.min_trade_pct = min_trade_pct
        self.increase_factor = increase_factor
        self.decrease_factor = decrease_factor
        self.current_allocation_pct = min_trade_pct

    def adjust_allocation(self, trade_history: List[Dict]) -> None:
        if not trade_history:
            return

        last_result = trade_history[-1]["result"]
        if last_result == "win":
            self.current_allocation_pct *= self.increase_factor
        elif last_result == "loss":
            self.current_allocation_pct *= self.decrease_factor

        self.current_allocation_pct = max(
            self.min_trade_pct, min(self.current_allocation_pct, self.max_trade_pct)
        )

    def allocate(self, decision: str, total_capital: float, trade_history: List[Dict]) -> float:
        self.adjust_allocation(trade_history)
        if decision == "BUY":
            return total_capital * self.current_allocation_pct
        else:
            return 0.0

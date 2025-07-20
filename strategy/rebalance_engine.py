import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class RebalanceEngine:
    def __init__(self):
        self.strategy_weights = {}
        self.active_positions = {}
        self.pnl_tracking = {}

    def register_strategy(self, name: str, weight: float) -> None:
        """Register or update a strategy with a specific weight."""
        if weight < 0:
            raise ValueError("Weight must be non-negative.")
        self.strategy_weights[name] = weight
        logger.debug(f"Registered strategy {name} with weight {weight}")

    def update_position(self, strategy: str, signal: str, pnl: float) -> None:
        """Update the current position and track PnL for a strategy."""
        self.active_positions[strategy] = signal
        self.pnl_tracking[strategy] = self.pnl_tracking.get(strategy, 0.0) + pnl
        logger.info(
            f"Strategy {strategy} position: {signal}, "
            f"cumulative PnL: {self.pnl_tracking[strategy]}"
        )

    def rebalance(self) -> Dict[str, Any]:
        """
        Rebalance all strategies based on weights and PnL.
        Returns new trade signals or allocations.
        """
        total_weight = sum(self.strategy_weights.values())
        if total_weight == 0:
            logger.warning("Total weight is zero; no rebalancing performed.")
            return {}

        normalized = {
            name: weight / total_weight for name, weight in self.strategy_weights.items()
        }

        rebalance_signals = {}
        for strategy, weight in normalized.items():
            signal = self._decide(strategy, weight)
            rebalance_signals[strategy] = signal
            logger.debug(f"Rebalanced {strategy} to signal: {signal}")

        return rebalance_signals

    def _decide(self, strategy: str, weight: float) -> str:
        """Internal logic for signal decision. Extend with RL/AI later."""
        current_pnl = self.pnl_tracking.get(strategy, 0.0)
        if current_pnl > 0 and weight >= 0.5:
            return "BUY"
        elif current_pnl < 0 and weight < 0.5:
            return "SELL"
        return "HOLD"

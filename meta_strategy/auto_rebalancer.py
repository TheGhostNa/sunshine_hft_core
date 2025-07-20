# meta_strategy/auto_rebalancer.py


def rebalance_equity(current_allocation, target_allocation, total_equity):
    """
    Calculates adjustments needed to align current allocation with target allocation.

    Returns a dict with symbol and adjustment quantity (+buy, -sell).
    """
    adjustments = {}
    for symbol in target_allocation:
        target_value = total_equity * target_allocation[symbol]
        current_value = current_allocation.get(symbol, 0)
        adjustments[symbol] = target_value - current_value
    return adjustments

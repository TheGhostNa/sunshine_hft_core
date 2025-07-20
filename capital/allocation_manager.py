# sunshine_hft_core/capital/allocation_manager.py


def get_allocated_amount(symbol: str, total_capital: float, risk_per_trade: float = 0.02):
    """
    Calculate the capital allocated to a specific trade.
    :param symbol: Stock symbol (e.g. AAPL)
    :param total_capital: Total capital available to trade
    :param risk_per_trade: Percentage of capital to risk on one trade
    :return: float - amount to allocate
    """
    allocated = total_capital * risk_per_trade
    print(f"[Capital] Allocated ${allocated:.2f} for {symbol}")
    return allocated

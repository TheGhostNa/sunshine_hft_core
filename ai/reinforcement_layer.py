def evaluate_strategy_performance(trade_log):
    """
    Evaluates how successful a trade strategy is based on recent trades.
    Returns a score between -1.0 (bad) to 1.0 (excellent).
    """
    if not trade_log:
        return 0.0

    profits = []
    for i in range(1, len(trade_log), 2):
        buy = trade_log[i - 1]
        sell = trade_log[i]
        if buy["type"] == "BUY" and sell["type"] == "SELL":
            pnl = sell["price"] - buy["price"]
            profits.append(pnl)

    if not profits:
        return 0.0

    avg_profit = sum(profits) / len(profits)
    score = max(-1.0, min(1.0, avg_profit / 100.0))  # Normalize
    return round(score, 2)


def adjust_capital_allocation(base_allocation, performance_score):
    """
    Adjusts HFT allocation based on performance score.
    - performance_score > 0 → boost HFT allocation
    - performance_score < 0 → reduce HFT allocation
    """
    hft_allocation = base_allocation
    hft_allocation += performance_score * 0.1  # ±10% max shift

    # Clamp between 0.3 and 0.9
    hft_allocation = max(0.3, min(0.9, hft_allocation))
    hold_allocation = 1.0 - hft_allocation

    return round(hft_allocation, 2), round(hold_allocation, 2)


# Example usage
if __name__ == "__main__":
    dummy_log = [
        {"type": "BUY", "price": 100, "index": 0},
        {"type": "SELL", "price": 105, "index": 1},
        {"type": "BUY", "price": 102, "index": 2},
        {"type": "SELL", "price": 101, "index": 3},
    ]

    score = evaluate_strategy_performance(dummy_log)
    print(f"Performance Score: {score}")

    hft, hold = adjust_capital_allocation(0.5, score)
    print(f"Adjusted Allocation — HFT: {hft}, HOLD: {hold}")

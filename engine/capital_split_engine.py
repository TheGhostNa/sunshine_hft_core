import numpy as np


def allocate_capital(total_capital, hold_ratio=0.5):
    """
    Split capital into HFT (trading) vs Long-Term Hold pool.
    hold_ratio: fraction to be allocated to long-term hold (0.0 to 1.0)
    """
    hold_capital = total_capital * hold_ratio
    hft_capital = total_capital - hold_capital
    return {
        "total": total_capital,
        "hold_ratio": hold_ratio,
        "hold_capital": hold_capital,
        "hft_capital": hft_capital,
    }


def dynamic_rebalance(price_history, threshold=0.03):
    """
    Adjust capital split based on recent returns.
    If market gains > threshold, increase hold pool.
    If market drops > threshold, reduce hold pool.
    """
    returns = np.diff(price_history) / price_history[:-1]
    recent_return = np.mean(returns[-5:])

    if recent_return > threshold:
        return min(0.9, 0.6 + recent_return)  # tilt toward holding
    elif recent_return < -threshold:
        return max(0.1, 0.4 + recent_return)  # tilt toward HFT (more active)
    else:
        return 0.5  # neutral hold ratio


def simulate_rebalance_loop(initial_capital, price_series):
    history = []
    current_capital = initial_capital
    for i in range(10, len(price_series)):
        window = price_series[i - 10: i]
        ratio = dynamic_rebalance(window)
        allocation = allocate_capital(current_capital, ratio)
        history.append(allocation)
    return history

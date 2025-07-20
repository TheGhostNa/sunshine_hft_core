def combine_signals(signal_dict):
    """
    Combines multiple strategy signals into one unified decision.

    Args:
        signal_dict (dict): {'rsi': 'buy', 'macd': 'hold', ...}

    Returns:
        str: Final combined signal - 'buy', 'sell', or 'hold'
    """
    weights = {"rsi": 0.5, "macd": 0.5}  # can be extended
    scores = {"buy": 1, "hold": 0, "sell": -1}

    total = 0
    for strat, sig in signal_dict.items():
        strat_weight = weights.get(strat, 0)
        score = scores.get(sig, 0)
        total += strat_weight * score

    if total > 0.2:
        return "buy"
    elif total < -0.2:
        return "sell"
    else:
        return "hold"

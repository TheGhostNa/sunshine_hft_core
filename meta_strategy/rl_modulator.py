# meta_strategy/rl_modulator.py


def reward_signal(symbol: str, trade_result: str) -> float:
    """
    Dummy reinforcement logic. Reward signal is positive for 'win' and negative for 'loss'.
    You can later enhance this with PnL, Sharpe ratio, etc.
    """
    if trade_result == "win":
        return 1.0
    elif trade_result == "loss":
        return -1.0
    else:
        return 0.0  # unknown or hold

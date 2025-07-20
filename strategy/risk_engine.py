# strategy/risk_engine.py

def apply_risk_filters(signal, position_open, cooldown=False):
    """Basic risk filter for signal decision."""
    if cooldown:
        return 'hold'
    if position_open and signal == 'buy':
        return 'hold'
    return signal

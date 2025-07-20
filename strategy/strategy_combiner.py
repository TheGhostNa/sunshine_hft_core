# strategy/strategy_combiner.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategy.rsi_strategy import rsi_signal
from strategy.macd_bb_strategy import macd_bb_signal

def combined_signal_generator(data):
    """Combine multiple strategy signals for final decision."""
    rsi = rsi_signal(data)
    macd_bb = macd_bb_signal(data)

    # Example: Reinforced logic (both must align)
    if rsi == macd_bb and rsi in ['buy', 'sell']:
        return rsi
    return 'hold'

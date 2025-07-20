# state/trade_state_manager.py

import time


class TradeStateManager:
    def __init__(self, cooldown=60):
        self.position = None  # 'LONG', 'SHORT', or None
        self.last_signal = None
        self.last_trade_time = 0
        self.cooldown = cooldown  # in seconds

    def can_trade(self):
        return (time.time() - self.last_trade_time) >= self.cooldown

    def update(self, signal):
        self.last_signal = signal
        self.last_trade_time = time.time()
        self.position = (
            "LONG" if signal == "BUY" else "SHORT" if signal == "SELL" else self.position
        )

    def reset(self):
        self.position = None
        self.last_signal = None
        self.last_trade_time = 0

import time


class CooldownTracker:
    def __init__(self, cooldown_seconds=300):
        self.last_trade_times = {}
        self.cooldown = cooldown_seconds

    def can_trade(self, asset):
        now = time.time()
        last_time = self.last_trade_times.get(asset, 0)
        return (now - last_time) >= self.cooldown

    def update(self, asset):
        self.last_trade_times[asset] = time.time()

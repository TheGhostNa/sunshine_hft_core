import time


class CooldownManager:
    def __init__(self, cooldown_seconds=60):
        self.cooldowns = {}
        self.cooldown_seconds = cooldown_seconds

    def is_in_cooldown(self, symbol):
        return time.time() < self.cooldowns.get(symbol, 0)

    def set_cooldown(self, symbol):
        self.cooldowns[symbol] = time.time() + self.cooldown_seconds

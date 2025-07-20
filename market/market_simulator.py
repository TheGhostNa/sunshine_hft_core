import time


class MarketSimulator:
    def __init__(self, close_prices, delay=1):
        self.close_prices = close_prices
        self.index = 0
        self.delay = delay  # in seconds

    def get_next_price(self):
        if self.index >= len(self.close_prices):
            return None  # End of data
        price = self.close_prices[self.index]
        self.index += 1
        time.sleep(self.delay)
        return price

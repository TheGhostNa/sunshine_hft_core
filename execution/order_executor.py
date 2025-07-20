class OrderExecutor:
    def __init__(self):
        self.positions = {}
        self.equity = 10000  # starting equity

    async def execute_orders(self, signals):
        # signals = dict e.g. {'buy': True, 'sell': False}
        if signals.get("buy"):
            qty = int(self.equity // 150)  # example position sizing
            print(f"[OPEN] Buying {qty} shares")
            # Place order logic here (paper or live)
            self.positions["AAPL"] = {"qty": qty, "avg_price": 150}
        if signals.get("sell") and "AAPL" in self.positions:
            qty = self.positions["AAPL"]["qty"]
            print(f"[CLOSE] Selling {qty} shares")
            # Close order logic here
            self.positions.pop("AAPL")

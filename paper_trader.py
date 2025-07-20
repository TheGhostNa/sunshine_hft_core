class PaperTrader:
    def __init__(self):
        self.balance = 100000
        self.position = None

    def buy(self, price):
        if not self.position:
            self.position = price
            print(f"[BUY] at ${price:.2f}")
        else:
            print("Already in position.")

    def sell(self, price):
        if self.position:
            profit = price - self.position
            self.balance += profit
            print(f"[SELL] at ${price:.2f}, Profit: ${profit:.2f}")
            self.position = None
        else:
            print("No position to sell.")

    def status(self):
        print(f"💰 Balance: ${self.balance:.2f}, Position: {self.position}")

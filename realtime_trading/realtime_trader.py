import time


class RealTimeTrader:
    def __init__(self, notifier):
        self.notifier = notifier
        self.equity = 10000  # Starting equity
        self.positions = {}

    def run(self):
        self.notifier.send_message("Realtime trader started.")
        # Dummy simulation loop (replace with real trading logic)
        for i in range(3):
            self.notifier.send_message(f"Trading iteration {i+1}")
            time.sleep(2)

        self.notifier.send_message("Realtime trader finished.")

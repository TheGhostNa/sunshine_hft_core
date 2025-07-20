class PositionTracker:
    def __init__(self):
        self.positions = {}

    def has_open_position(self, symbol):
        return self.positions.get(symbol, False)

    def open_position(self, symbol):
        self.positions[symbol] = True

    def close_position(self, symbol):
        self.positions[symbol] = False

from execution.live_trader import LiveTrader
from execution.paper_trader import PaperTrader


class TradeExecutor:
    def __init__(self, mode="paper"):
        self.mode = mode.lower()
        if self.mode == "live":
            self.trader = LiveTrader()
        else:
            self.trader = PaperTrader()

    def place_order(
        self, symbol, qty, side, order_type="market", limit_price=None, stop_price=None
    ):
        return self.trader.place_order(symbol, qty, side, order_type, limit_price, stop_price)

    def cancel_order(self, order_id):
        return self.trader.cancel_order(order_id)

    def get_open_orders(self, symbol):
        return self.trader.get_open_orders(symbol)

    def switch_mode(self, new_mode):
        self.mode = new_mode.lower()
        if self.mode == "live":
            self.trader = LiveTrader()
        else:
            self.trader = PaperTrader()

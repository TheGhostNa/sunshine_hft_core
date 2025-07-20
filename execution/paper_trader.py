import uuid


class PaperTrader:
    def __init__(self):
        self.orders = {}  # store orders as dict: order_id -> order_details

    def place_order(
        self, symbol, qty, side, order_type="market", limit_price=None, stop_price=None
    ):
        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "order_type": order_type,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "status": "filled",  # For paper trading, assume instant fill
        }
        self.orders[order_id] = order
        print(f"[PaperTrader] Order placed and filled: {order}")
        return order

    def cancel_order(self, order_id):
        if order_id in self.orders:
            self.orders[order_id]["status"] = "canceled"
            print(f"[PaperTrader] Order {order_id} canceled")
            return True
        print(f"[PaperTrader] Order {order_id} not found")
        return False

    def get_open_orders(self, symbol):
        return [o for o in self.orders.values() if o["symbol"] == symbol and o["status"] == "open"]

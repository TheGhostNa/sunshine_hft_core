from utils.alpaca_api import api


class LiveTrader:
    def place_order(
        self, symbol, qty, side, order_type="market", limit_price=None, stop_price=None
    ):
        try:
            order_params = {
                "symbol": symbol,
                "qty": qty,
                "side": side,
                "type": order_type,
                "time_in_force": "gtc",
            }
            if order_type == "limit" and limit_price:
                order_params["limit_price"] = limit_price
            if stop_price:
                order_params["stop_price"] = stop_price

            order = api.submit_order(**order_params)
            print(f"[LiveTrader] Order placed: {order}")
            return order
        except Exception as e:
            print(f"[LiveTrader] Failed to place order: {e}")
            return None

    def cancel_order(self, order_id):
        try:
            api.cancel_order(order_id)
            print(f"[LiveTrader] Order {order_id} canceled")
            return True
        except Exception as e:
            print(f"[LiveTrader] Failed to cancel order {order_id}: {e}")
            return False

    def get_open_orders(self, symbol):
        try:
            orders = api.list_orders(status="open", symbols=[symbol])
            return orders
        except Exception as e:
            print(f"[LiveTrader] Failed to get open orders: {e}")
            return []

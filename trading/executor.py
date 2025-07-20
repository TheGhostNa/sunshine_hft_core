from alpaca_trade_api.rest import REST

from config import APCA_API_KEY_ID, APCA_API_SECRET_KEY, BASE_URL


class TradeExecutor:
    def __init__(self, mode="paper"):
        self.mode = mode
        self.api = REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, BASE_URL, api_version="v2")

    def place_order(self, symbol, qty, side="buy"):
        print(
            f"💰 Placing {side.upper()} order for {qty} shares of {symbol} in {self.mode} mode..."
        )
        try:
            order = self.api.submit_order(
                symbol=symbol, qty=qty, side=side, type="market", time_in_force="gtc"
            )
            print(f"✅ Order placed: {order}")
            return order
        except Exception as e:
            print(f"❌ Order failed: {e}")
            return None

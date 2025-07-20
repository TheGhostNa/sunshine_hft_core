

class Trader:
    def __init__(self, api):
        self.api = api

    def submit_order(self, symbol, qty, side, type="market", time_in_force="gtc"):
        try:
            order = self.api.submit_order(
                symbol=symbol, qty=qty, side=side, type=type, time_in_force=time_in_force
            )
            print(f"✅ Order submitted: {side.upper()} {qty} shares of {symbol}")
            return order
        except Exception as e:
            print(f"❌ Error submitting order: {e}")
            return None

    def submit_oco_order(self, symbol, qty, side, take_profit, stop_loss):
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type="market",
                time_in_force="gtc",
                order_class="oco",
                take_profit={"limit_price": take_profit},
                stop_loss={"stop_price": stop_loss},
            )
            print(f"✅ OCO Order submitted: {side.upper()} {qty} shares of {symbol}")
            return order
        except Exception as e:
            print(f"❌ Error submitting OCO order: {e}")
            return None

    def get_position(self, symbol):
        try:
            position = self.api.get_position(symbol)
            print(f"📦 Position for {symbol}: {position.qty} shares at ${position.avg_entry_price}")
            return position
        except Exception as e:
            print(f"ℹ️ No existing position for {symbol}: {e}")
            return None

    def get_account_info(self):
        try:
            account = self.api.get_account()
            print("📊 Account info:")
            print(account._raw)
            return account._raw
        except Exception as e:
            print(f"❌ Error fetching account info: {e}")
            return None

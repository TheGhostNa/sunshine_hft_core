import os

from alpaca_trade_api.rest import REST
from dotenv import load_dotenv
from telegram_notifier import TelegramNotifier

from logger.trade_logger import TradeLogger

load_dotenv()


class ExecutionEngine:
    def __init__(self, mode="paper", strategy_name="Meta"):
        self.mode = mode
        self.api_key = os.getenv("APCA_API_KEY_ID")
        self.api_secret = os.getenv("APCA_API_SECRET_KEY")
        self.api_base_url = os.getenv("APCA_API_BASE_URL")
        self.notifier = TelegramNotifier()
        self.logger = TradeLogger(strategy_name)

        if not all([self.api_key, self.api_secret, self.api_base_url]):
            print("❌ ERROR: Missing API credentials in .env!")
            self.api = None
            self.api_base_url = None
        else:
            self.api = REST(self.api_key, self.api_secret, self.api_base_url)

        self.last_trade_price = {}

    def execute_trade(self, asset, action, qty):
        if action == "HOLD" or qty <= 0:
            print(f"⚪ No trade for {asset} (hold signal)")
            return

        try:
            # Get current market price
            barset = self.api.get_bars(asset, "minute", limit=1).df
            if barset.empty:
                print(f"⚠️ No price data for {asset}")
                return
            price = float(barset["close"].iloc[-1])
            value = round(price * qty, 2)

            # Fake execution logic (no real trade)
            print(f"✅ Executed {action} {qty} of {asset} @ ${price:.2f} (${value})")

            # Track profit
            previous_price = self.last_trade_price.get(asset)
            profit = 0
            if previous_price:
                if action == "BUY":
                    profit = -(price - previous_price) * qty
                elif action == "SELL":
                    profit = (price - previous_price) * qty

            self.last_trade_price[asset] = price

            # Log and notify
            self.logger.log_trade(asset, action, price, qty, profit)
            self.notifier.notify_trade(asset, action, price, qty)

        except Exception as e:
            error_msg = f"Trade error for {asset}: {e}"
            print(f"❌ {error_msg}")
            self.notifier.notify_error(error_msg)

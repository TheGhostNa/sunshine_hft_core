import os

import requests


class TelegramNotifier:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, message):
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message, "parse_mode": "HTML"}
        try:
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram error: {str(e)}")
            return False

    def notify_trade(self, asset, action, price, quantity):
        message = (
            f"🚀 <b>TRADE EXECUTED</b>\n"
            f"• Asset: {asset}\n"
            f"• Action: {action}\n"
            f"• Price: ${price:.2f}\n"
            f"• Quantity: {quantity}"
        )
        return self.send_message(message)

    def notify_error(self, error_msg):
        message = f"❌ <b>SYSTEM ERROR</b>\n{error_msg}"
        return self.send_message(message)


# Usage example
if __name__ == "__main__":
    notifier = TelegramNotifier()

    # On trade execution:
    notifier.notify_trade("TSLA", "SELL", 250.75, 15)

    # On error:
    notifier.notify_error("Connection lost with Alpaca API")

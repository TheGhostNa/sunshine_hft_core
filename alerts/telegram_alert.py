import requests


class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"}
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print("[✅] Telegram alert sent.")
            else:
                print(f"[❌] Telegram send error: {response.text}")
        except Exception as e:
            print(f"[❌] Telegram exception: {e}")


# === Example Usage ===
if __name__ == "__main__":
    BOT_TOKEN = "your_bot_token_here"
    CHAT_ID = "your_chat_id_here"
    notifier = TelegramNotifier(BOT_TOKEN, CHAT_ID)
    notifier.send_message("🚨 *Trade Alert*: AAPL BUY at 150.00 TP: 160 SL: 147")

import os

import requests


def send_telegram_message(message: str, parse_mode: str = "HTML"):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("⚠️ Missing Telegram credentials in environment.")
        return

    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message, "parse_mode": parse_mode}
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("✅ Telegram alert sent.")
    except Exception as e:
        print(f"❌ Telegram send error: {e}")

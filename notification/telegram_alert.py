# notification/telegram_alert.py

import os

import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_alert(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram credentials missing in .env")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"📣 Sunshine HFT Alert:\n{message}",
        "parse_mode": "Markdown",
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"❌ Telegram send error: {response.text}")
        else:
            print("✅ Telegram alert sent.")
    except Exception as e:
        print(f"❌ Telegram alert failed: {e}")

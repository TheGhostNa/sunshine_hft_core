# dashboard/telegram_report_sender.py

import os

import requests

# Load from environment or config
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")


def send_telegram_report(file_path, caption="📈 Strategy Report"):
    """Sends a file (HTML or PDF) to a Telegram chat."""
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN" or TELEGRAM_CHAT_ID == "YOUR_CHAT_ID":
        print("⚠️ Telegram not configured.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"

    try:
        with open(file_path, "rb") as doc:
            response = requests.post(
                url, data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption}, files={"document": doc}
            )

        if response.status_code == 200:
            print(f"✅ Telegram report sent: {file_path}")
        else:
            print(f"❌ Failed to send Telegram report: {response.text}")
    except Exception as e:
        print(f"❌ Telegram send error: {e}")

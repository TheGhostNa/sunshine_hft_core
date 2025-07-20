from notification.email_alert import send_email_alert
from utils.telegram_bot import send_telegram_message


def send_error_alert(module: str, error: str):
    message = f"🚨 <b>ERROR</b> in <b>{module}</b>\n\n❌ {error}"

    # Send to Telegram
    send_telegram_message(message)

    # Send to Email
    send_email_alert("🚨 Sunshine HFT Error", message)

# notification/test_alerts.py

from notification.email_alert import send_email_alert
from notification.telegram_alert import send_telegram_alert

send_telegram_alert("✅ Telegram alert is working!")
send_email_alert("✅ Email Test", "Sunshine HFT email alert is working fine.")

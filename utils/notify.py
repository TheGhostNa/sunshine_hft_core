# sunshine_hft_core/utils/notify.py

import smtplib
from email.message import EmailMessage

import requests

# Telegram setup
TELEGRAM_BOT_TOKEN = "8096648051:AAHxi7kcseUrOFWW4FkbT9ZcsGmNW9MHLf4"
TELEGRAM_CHAT_ID = "6890199002"

# Email setup (customize)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_email_password"  # Replace with app password or actual password


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Telegram error: {response.text}")
    except Exception as e:
        print(f"❌ Telegram notification failed: {e}")


def send_email(subject, body, to=EMAIL_ADDRESS):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"❌ Email notification failed: {e}")


def send_notification(message, send_tele=True, send_mail=False):
    if send_tele:
        send_telegram(message)
    if send_mail:
        send_email("Sunshine HFT Alert", message)

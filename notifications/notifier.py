# 📁 notifications/notifier.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from dotenv import load_dotenv

load_dotenv()


# Telegram Notification
def send_telegram_notification(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        print("❌ Telegram credentials not set.")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Telegram alert sent.")
        else:
            print(f"❌ Telegram alert failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram alert error: {e}")


# Email Notification
def send_email_notification(subject, body):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("TO_EMAIL")

    if not sender_email or not sender_password or not receiver_email:
        print("❌ Email credentials not set.")
        return

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email alert sent.")
    except Exception as e:
        print(f"❌ Email alert error: {e}")

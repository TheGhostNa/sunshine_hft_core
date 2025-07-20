import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")


def send_webhook_alert(message):
    if not WEBHOOK_URL:
        print("Webhook URL not set. Skipping webhook alert.")
        return
    # Send webhook alert logic here

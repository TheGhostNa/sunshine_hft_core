from notification.email_alert import send_email_alert
from notification.error_alert import send_error_alert
from notification.telegram_alert import send_telegram_alert


def test_all_alerts():
    print("🔔 Running Notification Unit Tests...\n")

    # 1. Telegram
    try:
        send_telegram_alert("📢 Telegram Test Passed ✅")
        print("✅ Telegram alert sent.")
    except Exception as e:
        print(f"❌ Telegram test failed: {e}")

    # 2. Email
    try:
        send_email_alert("Email Test", "✅ Email Test Passed")
        print("✅ Email alert sent.")
    except Exception as e:
        print(f"❌ Email test failed: {e}")

    # 3. Error Alert (Sends both Email + Telegram with context)
    try:
        module_name = "price_fetcher.py"
        error_msg = "TimeoutError"
        print(f"Sending error alert with module: {module_name} and error: {error_msg}")
        send_error_alert(module_name, error_msg)
        print("✅ Error alert sent.")
    except Exception as e:
        print(f"❌ Error alert test failed: {e}")


if __name__ == "__main__":
    test_all_alerts()

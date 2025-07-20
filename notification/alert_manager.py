import os

from notification.email_alert import send_email_alert
from notification.telegram_alert import send_telegram_alert


def send_trade_alert(symbol, signal, price):
    """
    Sends alerts (Telegram + Email) when a trade decision is made.

    Parameters:
    - symbol: str - stock/crypto symbol (e.g., 'AAPL')
    - signal: str - 'buy' or 'sell'
    - price: float - price at which trade is triggered
    """

    message = f"📣 Trade Signal Alert:\n\n🧠 Symbol: {symbol}\n📊 Action: {signal.upper()}\n💰 Price: ${price:.2f}"

    if os.getenv("TELEGRAM_NOTIFICATIONS", "no").lower() == "yes":
        send_telegram_alert(message)

    if os.getenv("EMAIL_NOTIFICATIONS", "no").lower() == "yes":
        subject = f"Trade Alert: {symbol} {signal.upper()}"
        send_email_alert(subject, message)

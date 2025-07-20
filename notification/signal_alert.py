def send_signal_alert(channel, symbol, strategy, signal):
    from notification.email_alert import send_email_alert
    from notification.telegram_alert import send_telegram_alert

    message = f"[{strategy.upper()}] Signal for {symbol}: {signal.upper()}"
    subject = f"{strategy.upper()} Signal Alert: {symbol} - {signal}"

    if channel in ("telegram", "both"):
        send_telegram_alert(message)
    if channel in ("email", "both"):
        send_email_alert(subject, message)

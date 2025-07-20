def send_risk_trigger_alert(symbol, level, trigger_type):
    from notification.email_alert import send_email_alert
    from notification.telegram_alert import send_telegram_alert

    msg = f"{trigger_type.upper()} Triggered on {symbol}: ${level}"
    send_telegram_alert(msg)
    send_email_alert(f"{trigger_type.upper()} Alert - {symbol}", msg)

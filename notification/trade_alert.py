def send_trade_alert(symbol, side, quantity, price):
    from notification.email_alert import send_email_alert
    from notification.telegram_alert import send_telegram_alert

    msg = f"TRADE EXECUTED: {side.upper()} {quantity} {symbol} @ ${price}"
    send_telegram_alert(msg)
    send_email_alert("Trade Executed", msg)



def send_daily_summary(pnl_summary):
    from notification.email_alert import send_email_alert
    from notification.telegram_alert import send_telegram_alert

    subject = "📊 Daily Trade Summary"
    message = f"Total Trades: {pnl_summary['trades']}\n"
    message += f"PnL: ${pnl_summary['pnl']}\n"
    message += f"Best Asset: {pnl_summary['best']}\nWorst Asset: {pnl_summary['worst']}"

    send_telegram_alert(message)
    send_email_alert(subject, message)

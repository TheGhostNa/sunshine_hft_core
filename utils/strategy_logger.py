import datetime


def log_signals(signal_name, signal_data):
    """
    Logs the signal with timestamp to console (or later to file/db).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {signal_name}: {signal_data}")

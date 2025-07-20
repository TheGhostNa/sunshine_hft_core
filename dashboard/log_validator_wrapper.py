from dashboard.log_integrity_checker import LogIntegrityChecker


def validate_all():
    logs = ["logs/rsi_trades.csv", "logs/macd_trades.csv", "logs/meta_trades.csv"]
    validator = LogIntegrityChecker(logs)
    result = validator.validate()
    if result:
        print("❌ Log validation failed:", result)
    else:
        print("✅ All logs passed validation.")

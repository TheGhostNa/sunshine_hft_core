# test_logger.py
from logger.trade_logger import TradeLogger

logger = TradeLogger("rsi")

# Simulate a trade log
logger.log_trade("AAPL", "BUY", 195.67, 15, profit=42.0)

print("✅ RSI trade logged successfully.")

# simulate_trades.py

from utils.trade_logger import TradeLogger

# Define loggers for each strategy
rsi_logger = TradeLogger("RSI", "logs/rsi_trades.csv")
macd_logger = TradeLogger("MACD+BB", "logs/macd_trades.csv")
meta_logger = TradeLogger("Meta", "logs/meta_trades.csv")

# Simulate dummy trades
rsi_logger.log_trade("AAPL", "BUY", price=190.25, quantity=10, profit=25.75)
rsi_logger.log_trade("TSLA", "SELL", price=850.75, quantity=5, profit=-15.30)

macd_logger.log_trade("AAPL", "SELL", price=195.10, quantity=8, profit=30.45)
macd_logger.log_trade("TSLA", "BUY", price=830.50, quantity=6, profit=12.80)

meta_logger.log_trade("GOOG", "BUY", price=2750.50, quantity=2, profit=45.10)

print("✅ Dummy trades simulated and logged to CSV.")

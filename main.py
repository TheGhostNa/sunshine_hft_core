import os
from dotenv import load_dotenv

# Load all credentials
load_dotenv()

# --- Imports from your modules ---
from fetchers.live_price_fetcher import fetch_live_price
from strategies.rsi_strategy import rsi_signal
from strategies.macd_bb_strategy import macd_bb_signal
from execution.executor import execute_trade
from meta.strategy_combiner import combined_signal
from notification.alert import send_alert
from logger.trade_logger import log_trade

def main():
    print("🚀 SUNSHINE HFT CORE SYSTEM LAUNCHED")

    symbol = "AAPL"
    price = fetch_live_price(symbol)
    rsi = rsi_signal(symbol)
    macd = macd_bb_signal(symbol)
    
    signal = combined_signal(rsi, macd)

    if signal in ["buy", "sell"]:
        result = execute_trade(symbol, signal)
        send_alert(f"{signal.upper()} order placed for {symbol} at {price}")
        log_trade(symbol, price, signal, result)
    else:
        print("📉 No signal generated. Market conditions not met.")

if __name__ == "__main__":
    main()

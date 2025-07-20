import os
import time

from dotenv import load_dotenv

from realtime_trading.paper_trader import PaperTrader

load_dotenv()


print(f"🧪 Loaded Key: {os.getenv('APCA_API_KEY_ID')}")
print("🚀 Sunshine HFT starting...")

symbols = os.getenv("SYMBOLS", "AAPL").split(",")
interval = int(os.getenv("INTERVAL", 60))

while True:
    for symbol in symbols:
        print(f"\n📈 Running trader for {symbol}")
        try:
            trader = PaperTrader(symbol)
            trader.run()
        except Exception as e:
            print(f"❌ Error trading {symbol}: {e}")
    print(f"\n⏱️ Sleeping {interval}s before next loop...")
    time.sleep(interval)

import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENV", "test").lower()

if env == "live":
    print("🌐 Running in LIVE mode")
else:
    print("🔬 Running in TEST (paper) mode")

modules = [
    "strategy.rsi_strategy",
    "strategy.macd_bb_strategy",
    "strategy.strategy_combiner",
    "strategy.risk_engine",
    "meta.meta_manager",
    "market.live_price_fetcher",
    "market.forex_price_fetcher",
    "execution.order_executor",
    "backtest.backtester",
    "reporting.logger",
    "reporting.pnl_tracker",
    "notification.alert_unit_test"
]

for module in modules:
    print(f"\n🔁 Running {module}...")
    try:
        subprocess.run(["python", "-m", module], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run {module}: {e}")

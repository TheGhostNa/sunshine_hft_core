import time
import traceback

from config import INTERVAL, SYMBOL
from market_feed.live_price_fetcher import get_live_price
from realtime_trading.order_executor import execute_trade
from strategy.meta_strategy_manager import get_meta_strategy_signal
from utils.logger import log_error, log_info
from utils.notifier import send_telegram_message

print(f"\n📡 Starting real-time signal loop for {SYMBOL}...\n")

while True:
    try:
        df, price, source = get_live_price(SYMBOL)

        try:
            log_info(f"💰 Live price resolved from {source}: {price:.2f}")
        except BaseException:
            log_info(f"Live price resolved from {source}: {price:.2f}")

        print(f"💰 Latest price: {price:.2f}")

        signal = get_meta_strategy_signal(df)

        try:
            log_info(f"📊 Meta signal: {signal}")
        except BaseException:
            log_info(f"Meta signal: {signal}")

        print(f"🧠 Reinforced strategy signal: {signal}\n")

        # Execute trade only if signal is not HOLD
        if signal != "HOLD":
            execute_trade(signal, price)

    except Exception as e:
        log_error(f"❌ Error in signal loop: {str(e)}")
        traceback.print_exc()
        send_telegram_message(f"❌ Error in signal loop:\n{traceback.format_exc()}")

    time.sleep(INTERVAL)

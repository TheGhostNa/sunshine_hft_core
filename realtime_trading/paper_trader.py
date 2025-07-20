# realtime_trading/paper_trader.py

from meta_strategy.adaptive_signal_tuner import adjust_signal_strength
from meta_strategy.auto_rebalancer import rebalance_equity
from meta_strategy.meta_logger import log_meta_strategy
from meta_strategy.meta_signal_combiner import combine_signals
from meta_strategy.rl_modulator import reward_signal
from meta_strategy.strategy_score_tracker import update_strategy_score
from meta_strategy.time_weight_adjuster import time_weight_adjust
from notification.alert_manager import send_trade_alert
from realtime_trading.data_fetcher import fetch_latest_data
from technical_analysis.rsi_strategy import generate_rsi_signal
from utils.order_executor import get_trade_quantity, place_order


class PaperTrader:
    def __init__(self, symbol):
        self.symbol = symbol

    def run(self):
        try:
            data = fetch_latest_data(self.symbol)
            if not data or "df" not in data:
                print(f"⚠️ No data returned for {self.symbol}")
                return

            df = data["df"]

            print(f"📊 RSI input preview: {df.tail(3)}")

            # === STEP 1: Raw Strategy Signals ===
            rsi_signal = generate_rsi_signal(df, self.symbol)

            # === STEP 2: Meta-Strategy Combinations ===
            combined_signal = combine_signals([rsi_signal])
            adjusted_signal = adjust_signal_strength(combined_signal, df)
            rewarded_signal = reward_signal(adjusted_signal)
            final_signal = time_weight_adjust(rewarded_signal)

            # === STEP 3: Capital Allocation + Rebalancing ===
            quantity = get_trade_quantity(df, self.symbol)
            rebalance_equity()

            print(f"📊 Signal for {self.symbol}: {final_signal} | Qty: {quantity}")

            if final_signal != "hold":
                order_response = place_order(self.symbol, final_signal, quantity)
                send_trade_alert(self.symbol, final_signal, quantity, order_response)

            update_strategy_score(self.symbol, final_signal)
            log_meta_strategy(self.symbol, final_signal)

        except Exception as e:
            print(f"❌ Error trading {self.symbol}: {e}")

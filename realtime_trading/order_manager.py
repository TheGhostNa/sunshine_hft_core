# File: sunshine_hft_core/realtime_trading/order_manager.py

import time

from alpaca_trade_api.rest import REST

from config import APCA_API_KEY_ID, APCA_API_SECRET_KEY, BASE_URL

api = REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, BASE_URL, api_version="v2")


def monitor_and_exit(symbol, entry_price, qty, stop_loss_pct=0.01, take_profit_pct=0.02):
    """
    Monitors a position and triggers stop-loss or take-profit.
    """
    stop_loss_price = entry_price * (1 - stop_loss_pct)
    take_profit_price = entry_price * (1 + take_profit_pct)
    print(f"📉 Monitoring {symbol} | SL: {stop_loss_price:.2f}, TP: {take_profit_price:.2f}")

    while True:
        try:
            barset = api.get_latest_trade(symbol)
            current_price = float(barset.price)
            print(f"🔄 Current Price: {current_price}", end="\r")

            if current_price <= stop_loss_price:
                print(f"🚨 Stop Loss Hit at {current_price}, selling...")
                api.submit_order(
                    symbol=symbol, qty=qty, side="sell", type="market", time_in_force="day"
                )
                break

            elif current_price >= take_profit_price:
                print(f"🚀 Take Profit Hit at {current_price}, selling...")
                api.submit_order(
                    symbol=symbol, qty=qty, side="sell", type="market", time_in_force="day"
                )
                break

            time.sleep(5)

        except Exception as e:
            print(f"❌ Error in monitor loop: {e}")
            time.sleep(10)

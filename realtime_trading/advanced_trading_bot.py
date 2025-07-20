import time

from alpaca_trade_api.rest import REST

from config.alpaca_keys import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL
from strategies.alpha_models import generate_signals
from utils.notifications import send_telegram

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)

equity = 10000  # Starting paper equity
positions = {}

SYMBOL = "AAPL"
QTY = 10
TP_PERCENT = 0.03
SL_PERCENT = 0.02


def place_order(symbol, qty, side, sl=None, tp=None):
    if side == "buy":
        order = api.submit_order(
            symbol=symbol, qty=qty, side="buy", type="market", time_in_force="gtc"
        )
        if sl and tp:
            print(f"Setting manual SL/TP for {symbol} at SL={sl} TP={tp}")
        return order
    else:
        return api.submit_order(
            symbol=symbol, qty=qty, side="sell", type="market", time_in_force="gtc"
        )


def check_exit(symbol):
    position = positions.get(symbol)
    if not position:
        return
    current_price = api.get_last_trade(symbol).price
    avg_price = position["avg_price"]
    sl = avg_price * (1 - SL_PERCENT)
    tp = avg_price * (1 + TP_PERCENT)
    if current_price <= sl or current_price >= tp:
        print(f"[CLOSE] {symbol} current={current_price} triggered SL/TP")
        place_order(symbol, 1, "sell")
        del positions[symbol]
        send_telegram(f"Trade closed: {symbol} at {current_price}")


def run_bot():
    while True:
        signals = generate_signals(SYMBOL)
        if signals.get("buy") and SYMBOL not in positions:
            last_price = api.get_last_trade(SYMBOL).price
            place_order(SYMBOL, QTY, "buy")
            positions[SYMBOL] = {"qty": QTY, "avg_price": last_price}
            send_telegram(f"Opened position: {SYMBOL} at {last_price}")

        check_exit(SYMBOL)
        time.sleep(60)


if __name__ == "__main__":
    run_bot()

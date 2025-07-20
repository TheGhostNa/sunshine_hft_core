import time


def execute_signals(api, symbol, buy_signals, sell_signals, prices):
    position = None

    for i in range(len(prices)):
        if buy_signals[i] == 1 and position is None:
            qty = 1  # ⚠️ Adjust quantity if needed
            api.submit_order(symbol=symbol, qty=qty, side="buy", type="market", time_in_force="gtc")
            print(f"✅ Executed BUY at index {i}, price {prices[i]}")
            position = "long"

        elif sell_signals[i] == 1 and position == "long":
            qty = 1
            api.submit_order(
                symbol=symbol, qty=qty, side="sell", type="market", time_in_force="gtc"
            )
            print(f"✅ Executed SELL at index {i}, price {prices[i]}")
            position = None

        # simulate delay between signals (for live mode)
        time.sleep(0.5)

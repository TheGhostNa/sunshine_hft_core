import numpy as np


def hold_trade_logic(
    buy_signals, sell_signals, prices, hold_ratio=0.4, trade_ratio=0.5, reinvest_ratio=0.1
):
    held_assets = []
    traded_assets = []
    reinvested_value = 0
    cash = 10000
    trade_log = []

    for i in range(len(prices)):
        buy_price = buy_signals[i]
        sell_price = sell_signals[i]

        # Handle Buy Logic
        if isinstance(buy_price, (float, np.float64)):
            decision = np.random.choice(["hold", "trade"], p=[hold_ratio, trade_ratio])
            if decision == "hold":
                held_assets.append({"price": buy_price, "index": i})
            else:
                traded_assets.append({"price": buy_price, "index": i, "type": "buy"})

        # Handle Sell Logic
        if isinstance(sell_price, (float, np.float64)):
            for asset in traded_assets:
                if asset["type"] == "buy":
                    pnl = sell_price - asset["price"]
                    cash += sell_price  # assume 1 unit
                    reinvest_value = pnl * reinvest_ratio
                    reinvested_value += reinvest_value
                    cash -= reinvest_value
                    cash + reinvested_value
                    trade_log.append(
                        {
                            "buy_price": asset["price"],
                            "sell_price": sell_price,
                            "pnl": pnl,
                            "reinvested": reinvest_value,
                            "index": i,
                        }
                    )
                    asset["type"] = "sold"
                    break

    held_value = sum([a["price"] for a in held_assets])
    final_value = cash + held_value + reinvested_value

    return trade_log, final_value

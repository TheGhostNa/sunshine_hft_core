import os


def allocate_capital(total_equity, current_pnl):
    hold_pct = 0.4
    trade_pct = 0.5
    reinvest_pct = 0.1

    hold_amount = total_equity * hold_pct
    trade_amount = total_equity * trade_pct
    reinvest_amount = total_equity * reinvest_pct

    allocation = {
        "hold": hold_amount,
        "trade": trade_amount,
        "reinvest": reinvest_amount,
        "black_alpha_reserve": 0,
    }

    if os.getenv("BLACK_ALPHA_ENABLED", "no").lower() == "yes":
        try:
            threshold = float(os.getenv("BLACK_ALPHA_THRESHOLD", 100))
            percent = float(os.getenv("BLACK_ALPHA_PERCENT", 0.25))
            if current_pnl > threshold:
                reserve = current_pnl * percent
                allocation["black_alpha_reserve"] = reserve
        except Exception as e:
            print(f"⚠️ Black Alpha config error: {e}")

    return allocation

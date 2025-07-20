import json
import os
from datetime import datetime

PAYOUT_LOG = "portfolio/pnl_log.json"

# Ensure folder exists
os.makedirs("portfolio", exist_ok=True)


def update_pnl(symbol, price, signal):
    pnl_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "symbol": symbol,
        "price": price,
        "signal": signal,
    }

    if not os.path.exists(PAYOUT_LOG):
        with open(PAYOUT_LOG, "w") as f:
            json.dump([pnl_entry], f, indent=2)
        print("💹 PnL initialized.")
        return

    try:
        with open(PAYOUT_LOG, "r") as f:
            data = json.load(f)
    except Exception:
        data = []

    data.append(pnl_entry)

    with open(PAYOUT_LOG, "w") as f:
        json.dump(data, f, indent=2)

    print(f"💹 PnL updated: {signal} at {price}")

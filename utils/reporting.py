import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
TRADE_JSON = LOG_DIR / "trades.json"


def load_trades():
    with open(TRADE_JSON, "r") as f:
        return json.load(f)


def generate_summary():
    trades = load_trades()
    total_trades = len(trades)
    total_buy = sum(t["capital_used"] for t in trades if t["action"].lower() == "buy")
    total_sell = sum(t["capital_used"] for t in trades if t["action"].lower() == "sell")
    profit_loss = total_sell - total_buy

    # Calculate first and last trade times
    if trades:
        first_trade = datetime.fromisoformat(trades[0]["timestamp"])
        last_trade = datetime.fromisoformat(trades[-1]["timestamp"])
        duration = (last_trade - first_trade).total_seconds() / 3600  # in hours
    else:
        duration = 0

    summary = {
        "total_trades": total_trades,
        "total_buy_amount": total_buy,
        "total_sell_amount": total_sell,
        "net_profit_loss": profit_loss,
        "trading_duration_hours": duration,
    }
    return summary


def print_report():
    summary = generate_summary()
    print("=== TRADE SUMMARY REPORT ===")
    print(f"Total trades executed: {summary['total_trades']}")
    print(f"Total Buy amount: ${summary['total_buy_amount']:.2f}")
    print(f"Total Sell amount: ${summary['total_sell_amount']:.2f}")
    print(f"Net Profit/Loss: ${summary['net_profit_loss']:.2f}")
    print(f"Total trading duration: {summary['trading_duration_hours']:.2f} hours")

import json
import os

PORTFOLIO_PATH = "data/portfolio.json"

DEFAULT_PORTFOLIO = {"cash": 10000.0, "positions": {}, "risk_per_trade": 0.02}  # 2% per trade


def load_portfolio():
    if not os.path.exists(PORTFOLIO_PATH):
        save_portfolio(DEFAULT_PORTFOLIO)
    with open(PORTFOLIO_PATH, "r") as f:
        return json.load(f)


def save_portfolio(portfolio):
    with open(PORTFOLIO_PATH, "w") as f:
        json.dump(portfolio, f, indent=2)


def get_trade_amount(symbol: str, decision: str, price: float):
    portfolio = load_portfolio()
    cash = portfolio["cash"]
    risk = portfolio["risk_per_trade"]

    if decision == "BUY":
        allocation = cash * risk
        qty = int(allocation / price)
        print(f"💡 Allocating ${allocation:.2f} → {qty} shares of {symbol}")
        return qty
    elif decision == "SELL":
        return portfolio["positions"].get(symbol, 0)
    else:
        return 0


def update_portfolio(symbol, decision, qty, price):
    portfolio = load_portfolio()
    if decision == "BUY":
        cost = qty * price
        portfolio["cash"] -= cost
        portfolio["positions"][symbol] = portfolio["positions"].get(symbol, 0) + qty
    elif decision == "SELL":
        proceeds = qty * price
        portfolio["cash"] += proceeds
        portfolio["positions"][symbol] = max(0, portfolio["positions"].get(symbol, 0) - qty)
    save_portfolio(portfolio)

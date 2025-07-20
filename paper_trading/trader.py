# trader.py
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

API_KEY = "CK508HHELBVVTEPOL24P"
API_SECRET = "KNbzOQu1rSfLKRUpTVp8kcwSB6MRGfEJermza9PE"

# Use paper trading
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)


def place_order(symbol, qty=1, side="buy"):
    try:
        order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
        )
        order = trading_client.submit_order(order_data)
        print(f"✅ Order submitted: {order.id} | {side.upper()} {qty} shares of {symbol}")
    except Exception as e:
        print(f"❌ Order placement failed: {e}")


def get_account_info():
    account = trading_client.get_account()
    print(f"🔍 Account Status: {account.status} | Buying Power: {account.buying_power}")
    return account


def get_market_status():
    clock = trading_client.get_clock()
    print(f"🕒 Market Open: {clock.is_open} | Next Open: {clock.next_open}")
    return clock

import os

from alpaca_trade_api.rest import REST

# ✅ Load Alpaca keys from environment
MODE = os.getenv("MODE", "paper")
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# ✅ Setup Alpaca client
api = REST(API_KEY, API_SECRET, BASE_URL)


def place_order(symbol, qty, side, take_profit=None, stop_loss=None):
    """
    Place an order using Alpaca API, with optional OCO stop-loss and take-profit.

    Args:
        symbol (str): Stock symbol
        qty (int): Number of shares
        side (str): 'buy' or 'sell'
        take_profit (float): Optional take-profit price
        stop_loss (float): Optional stop-loss price
    """
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc",
            order_class="bracket" if take_profit and stop_loss else "simple",
            take_profit={"limit_price": take_profit} if take_profit else None,
            stop_loss=(
                {"stop_price": stop_loss, "limit_price": stop_loss * 0.98} if stop_loss else None
            ),
        )
        print(f"✅ Order placed for {symbol}: {side.upper()} {qty} shares")
        return order
    except Exception as e:
        print(f"❌ Order failed for {symbol}: {e}")
        return None


def get_trade_quantity(equity, price):
    """
    Calculate the number of shares to trade based on equity and price.
    Ensures at least 1 share is traded if affordable.

    Args:
        equity (float): Total capital allocated for this trade.
        price (float): Current price of the asset.

    Returns:
        int: Number of shares to trade.
    """
    if price <= 0:
        return 0
    qty = int(equity // price)
    return max(qty, 1)

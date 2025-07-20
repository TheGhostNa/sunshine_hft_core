# sunshine_hft_core/utils/execution.py


def execute_trade(symbol, action, price, allocated_amount):
    """
    Execute the trade action. This is a placeholder for actual broker API logic.
    :param symbol: Stock symbol
    :param action: BUY / SELL / HOLD
    :param price: Current market price
    :param allocated_amount: Capital allocated for this trade
    """
    if action == "BUY":
        shares = allocated_amount // price
        print(f"💰 Executing BUY for {shares} shares of {symbol} at ${price:.2f}")
    elif action == "SELL":
        print(f"💼 Executing SELL of {symbol} at ${price:.2f}")
    else:
        print("⚠️ HOLD: No action taken.")

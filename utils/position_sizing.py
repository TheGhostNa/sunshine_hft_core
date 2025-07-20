def calculate_position_size(equity, risk_per_trade, stop_loss_distance, price):
    """
    Calculate position size based on risk per trade and stop loss distance.
    :param equity: Total equity available.
    :param risk_per_trade: Percentage of equity to risk per trade (e.g. 0.01 for 1%)
    :param stop_loss_distance: Difference between entry price and stop loss price.
    :param price: Entry price.
    :return: Number of shares to buy/sell.
    """
    risk_amount = equity * risk_per_trade
    if stop_loss_distance == 0:
        return 0  # Avoid division by zero
    position_size = risk_amount / stop_loss_distance
    return int(position_size)

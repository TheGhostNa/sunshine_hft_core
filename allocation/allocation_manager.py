def allocate_capital(symbol, action):
    capital = 10000
    allocation = 0.1 * capital  # allocate 10%
    print(f"💰 Allocated ${allocation:.2f} to {action} {symbol}")
    return allocation

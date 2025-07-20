symbol_strategies = {"SPY": ["rsi", "macd_bb"], "MSFT": ["macd_bb"], "NVDA": ["rsi"]}


def get_strategies_for_symbol(symbol):
    return symbol_strategies.get(symbol, ["rsi"])

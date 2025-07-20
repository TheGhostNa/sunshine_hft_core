from strategy_manager.rsi_strategy import rsi_decision


def decide_trade_action(symbol, close_prices):
    # Currently only RSI strategy included, can add more signals here later
    decision = rsi_decision(close_prices)
    print(f"🧠 Meta-Strategy Decision based on RSI for {symbol}: {decision}")
    return decision

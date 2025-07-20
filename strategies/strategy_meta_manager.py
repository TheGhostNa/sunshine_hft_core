# === File: sunshine_hft_core/strategy/strategy_meta_manager.py ===
def combine_signals(rsi_buy, rsi_sell, macd_buy, macd_sell):
    combined_buy = []
    combined_sell = []
    length = min(len(rsi_buy), len(macd_buy))

    for i in range(length):
        buy = 1 if rsi_buy[i] == 1 or macd_buy[i] == 1 else 0
        sell = 1 if rsi_sell[i] == 1 or macd_sell[i] == 1 else 0
        combined_buy.append(buy)
        combined_sell.append(sell)

    return combined_buy, combined_sell

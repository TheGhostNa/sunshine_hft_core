from utils.trade_logger import generate_summary

for strategy in ["rsi_strategy", "macd_bb_strategy", "meta_strategy"]:
    generate_summary(strategy)

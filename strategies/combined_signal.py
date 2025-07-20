def get_combined_signals(df):
    from strategies.macd_bb_strategy import generate_macd_bb_signal
    from strategies.rsi_strategy import generate_rsi_signal

    return {"rsi": generate_rsi_signal(df), "macd_bb": generate_macd_bb_signal(df)}

import talib
import pandas as pd

def generate_rsi_signal(df, period=14, overbought=70, oversold=30):
    if 'Close' not in df.columns:
        raise ValueError("Missing 'Close' column in DataFrame.")
        
    rsi = talib.RSI(df['Close'], timeperiod=period)
    
    if rsi.empty or rsi.isna().all():
        return "hold"

    last_rsi = rsi.iloc[-1]

    if last_rsi > overbought:
        return "sell"
    elif last_rsi < oversold:
        return "buy"
    else:
        return "hold"

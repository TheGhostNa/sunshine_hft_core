# strategy/reinforce_modulator.py


def reinforce_signals(rsi_signal, macd_signal):
    if rsi_signal == macd_signal:
        return rsi_signal
    if rsi_signal == "BUY" and macd_signal == "HOLD":
        return "BUY"
    if rsi_signal == "SELL" and macd_signal == "HOLD":
        return "SELL"
    if rsi_signal == "HOLD" and macd_signal in ["BUY", "SELL"]:
        return macd_signal
    return "HOLD"

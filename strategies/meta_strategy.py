def generate_meta_signal(rsi_signal, macd_signal):
    if rsi_signal == macd_signal:
        return rsi_signal
    return "HOLD"


__all__ = ["generate_meta_signal"]

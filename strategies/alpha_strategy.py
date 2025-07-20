import talib


class AlphaStrategy:
    def __init__(self, df):
        self.df = df

    def generate_signal(self):
        close = self.df["c"].values
        rsi = talib.RSI(close, timeperiod=14)
        macd, macdsignal, _ = talib.MACD(close)
        upper, middle, lower = talib.BBANDS(close)

        if rsi[-1] < 30 and macd[-1] > macdsignal[-1] and close[-1] < lower[-1]:
            return "buy"
        elif rsi[-1] > 70 and macd[-1] < macdsignal[-1] and close[-1] > upper[-1]:
            return "sell"
        else:
            return "hold"

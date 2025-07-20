

class AlphaStrategy:
    def __init__(self, df):
        self.df = df

    def generate_signals(self):
        self.df["ma_short"] = self.df["close"].rolling(window=5).mean()
        self.df["ma_long"] = self.df["close"].rolling(window=15).mean()

        signals = []
        for i in range(len(self.df)):
            if i == 0:
                signals.append(0)
            else:
                if (
                    self.df["ma_short"].iloc[i] > self.df["ma_long"].iloc[i]
                    and self.df["ma_short"].iloc[i - 1] <= self.df["ma_long"].iloc[i - 1]
                ):
                    signals.append(1)
                elif (
                    self.df["ma_short"].iloc[i] < self.df["ma_long"].iloc[i]
                    and self.df["ma_short"].iloc[i - 1] >= self.df["ma_long"].iloc[i - 1]
                ):
                    signals.append(-1)
                else:
                    signals.append(0)
        return signals

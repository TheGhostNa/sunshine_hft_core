class CapitalSplitter:
    def split(self, total_capital):
        X1 = total_capital * 0.4  # Safe capital (e.g. in bond, stable assets)
        X2 = total_capital * 0.6  # High-risk, used for recursive AI trading
        return X1, X2

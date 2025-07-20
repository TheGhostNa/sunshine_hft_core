from utils.logger import get_logger


class TradeExecutor:
    def __init__(self):
        self.positions = {}
        self.logger = get_logger()

    def execute(self, symbol, signal, df):
        price = df["c"].iloc[-1]
        if signal == "buy":
            self.positions[symbol] = {"price": price, "qty": 10}
            self.logger.info(f"BUY {symbol} at {price}")
        elif signal == "sell" and symbol in self.positions:
            bought_price = self.positions[symbol]["price"]
            profit = (price - bought_price) * self.positions[symbol]["qty"]
            self.logger.info(f"SELL {symbol} at {price} | Profit: {profit:.2f}")
            del self.positions[symbol]
        else:
            self.logger.info(f"HOLD {symbol} at {price}")

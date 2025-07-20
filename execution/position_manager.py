# execution/position_manager.py


class PositionManager:
    def __init__(self, initial_equity=10000):
        self.equity = initial_equity
        self.positions = {}  # {symbol: {qty, avg_price, stop_loss, take_profit}}
        self.trade_log = []

    def open_position(self, symbol, qty, price, stop_loss=None, take_profit=None):
        if symbol in self.positions:
            pos = self.positions[symbol]
            total_qty = pos["qty"] + qty
            pos["avg_price"] = (pos["avg_price"] * pos["qty"] + price * qty) / total_qty
            pos["qty"] = total_qty
            if stop_loss is not None:
                pos["stop_loss"] = stop_loss
            if take_profit is not None:
                pos["take_profit"] = take_profit
        else:
            self.positions[symbol] = {
                "qty": qty,
                "avg_price": price,
                "stop_loss": stop_loss,
                "take_profit": take_profit,
            }
        self.trade_log.append(
            f"OPEN {symbol} qty={qty} price={price} SL={stop_loss} TP={take_profit}"
        )
        print(f"[OPEN] {symbol} qty={qty} avg_price={price} SL={stop_loss} TP={take_profit}")

    def close_position(self, symbol, qty, price):
        if symbol not in self.positions or self.positions[symbol]["qty"] < qty:
            print(f"[ERROR] Cannot close position for {symbol} - insufficient qty")
            return 0

        pos = self.positions[symbol]
        pnl = (price - pos["avg_price"]) * qty
        pos["qty"] -= qty
        self.equity += pnl
        self.trade_log.append(f"CLOSE {symbol} qty={qty} price={price} PnL={pnl:.2f}")
        print(
            f"[CLOSE] {symbol} qty={qty} exit_price={price} PnL={pnl:.2f} Equity={self.equity:.2f}"
        )

        if pos["qty"] == 0:
            del self.positions[symbol]

        return pnl

    def get_positions(self):
        return self.positions

    def get_equity(self):
        return self.equity

    def print_trade_log(self):
        print("\nTrade Log:")
        for entry in self.trade_log:
            print(" -", entry)

    def size_position(self, price, risk_per_trade=0.01, stop_loss_pct=0.02):
        risk_amount = self.equity * risk_per_trade
        stop_loss_amount = price * stop_loss_pct
        if stop_loss_amount == 0:
            return 0
        qty = risk_amount / stop_loss_amount
        return max(1, int(qty))

pnl_memory = 0.0


def update_profit(current_equity, initial_equity):
    global pnl_memory
    pnl = current_equity - initial_equity
    pnl_memory = pnl
    return pnl


def get_pnl():
    return pnl_memory

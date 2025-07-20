import matplotlib.pyplot as plt


def plot_signals(close_prices, buy_signals, sell_signals):
    """
    Plot close prices with buy and sell signals.

    Args:
        close_prices (list or np.ndarray): Close prices array.
        buy_signals (list[int]): 1 = buy signal, else 0.
        sell_signals (list[int]): 1 = sell signal, else 0.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(close_prices, label="Close Price", color="blue")

    buy_x = [i for i, val in enumerate(buy_signals) if val == 1]
    buy_y = [close_prices[i] for i in buy_x]
    plt.scatter(buy_x, buy_y, marker="^", color="green", label="Buy Signal", s=100)

    sell_x = [i for i, val in enumerate(sell_signals) if val == 1]
    sell_y = [close_prices[i] for i in sell_x]
    plt.scatter(sell_x, sell_y, marker="v", color="red", label="Sell Signal", s=100)

    plt.title("Price with Buy/Sell Signals")
    plt.xlabel("Index")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

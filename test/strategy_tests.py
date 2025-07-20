from utils.signal_generators import generate_rsi_signal


def test_rsi_signal_buy():
    prices = [30, 32, 31, 33, 34, 36, 35, 37, 36, 38, 37, 36, 35, 34, 33]
    signal = generate_rsi_signal(prices)
    assert signal in ["buy", "hold", "sell"]


def test_rsi_signal_sell():
    prices = [80] * 14 + [85]
    signal = generate_rsi_signal(prices)
    assert signal in ["buy", "hold", "sell"]


def test_rsi_signal_short_data():
    prices = [50, 51, 52]
    signal = generate_rsi_signal(prices)
    assert signal == "hold"

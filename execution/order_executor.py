# execution/order_executor.py

def simulate_order_execution(signal, price):
    """
    Simulates the execution of a trade based on the signal and price.
    This is a stub for backtesting. Replace with real execution logic if needed.
    """
    print(f"[SIMULATED ORDER] Signal: {signal}, Price: {price}")
    return {
        'signal': signal,
        'price': price,
        'status': 'executed'
    }

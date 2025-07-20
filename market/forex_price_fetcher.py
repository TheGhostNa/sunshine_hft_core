# market/forex_price_fetcher.py

import requests

def fetch_forex_price(pair="EURUSD"):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": pair[:3],
        "to_currency": pair[3:],
        "apikey": "YOUR_ALPHA_VANTAGE_API_KEY"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    except Exception as e:
        print(f"Forex price fetch error: {e}")
        return None

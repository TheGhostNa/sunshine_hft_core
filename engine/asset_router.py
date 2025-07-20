from data.crypto_price_fetcher import get_crypto_data
from data.stock_price_fetcher import get_stock_data


def route_asset_data(asset_type, symbol):
    if asset_type == "stocks":
        return get_stock_data(symbol)
    elif asset_type == "crypto":
        return get_crypto_data(symbol)
    else:
        raise ValueError(f"Unsupported asset type: {asset_type}")

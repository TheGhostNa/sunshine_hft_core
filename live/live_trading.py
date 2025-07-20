import asyncio
import os

import numpy as np
from alpaca_trade_api.rest import REST
from alpaca_trade_api.stream import Stream
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

symbol = "AAPL"

rest_api = REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")


class LiveTrader:
    def __init__(self):
        self.prices = []
        self.position = 0  # 0 = no position, 1 = holding
        self.entry_price = 0.0

    async def handle_trade(self, trade):
        price = trade.price
        self.prices.append(price)
        if len(self.prices) > 100:
            self.prices.pop(0)

        # Simple example: buy if last price > 50 SMA, sell if below
        sma = np.mean(self.prices)
        if self.position == 0 and price > sma:
            print(f"Buying at {price}")
            self.buy_order()
        elif self.position == 1 and price < sma:
            print(f"Selling at {price}")
            self.sell_order()

    def buy_order(self):
        if self.position == 0:
            rest_api.submit_order(
                symbol=symbol, qty=1, side="buy", type="market", time_in_force="gtc"
            )
            self.position = 1
            self.entry_price = self.prices[-1]

    def sell_order(self):
        if self.position == 1:
            rest_api.submit_order(
                symbol=symbol, qty=1, side="sell", type="market", time_in_force="gtc"
            )
            self.position = 0


async def main():
    trader = LiveTrader()
    stream = Stream(API_KEY, API_SECRET, base_url=BASE_URL, data_feed="iex")

    stream.subscribe_trades(trader.handle_trade, symbol)

    await stream._run_forever()


if __name__ == "__main__":
    asyncio.run(main())

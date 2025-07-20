# feed/alpaca_stream.py

import asyncio
import json

import websockets

from config.alpaca_keys import ALPACA_API_KEY, ALPACA_SECRET_KEY

ALPACA_FEED_URL = "wss://stream.data.alpaca.markets/v2/iex"  # for free account
SUBSCRIBE_SYMBOLS = ["AAPL", "TSLA", "MSFT"]  # Edit as needed


async def connect_to_stream():
    async with websockets.connect(ALPACA_FEED_URL) as ws:
        auth_msg = {"action": "auth", "key": ALPACA_API_KEY, "secret": ALPACA_SECRET_KEY}
        await ws.send(json.dumps(auth_msg))

        listen_msg = {"action": "subscribe", "trades": SUBSCRIBE_SYMBOLS}
        await ws.send(json.dumps(listen_msg))

        print(f"📡 Subscribed to: {SUBSCRIBE_SYMBOLS}")
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            print("📈 Tick:", data)


if __name__ == "__main__":
    asyncio.run(connect_to_stream())

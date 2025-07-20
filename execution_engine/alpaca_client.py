# execution_engine/alpaca_client.py

import os

import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

load_dotenv()

mode = os.getenv("MODE", "paper").lower()

if mode == "live":
    API_KEY = os.getenv("LIVE_API_KEY")
    SECRET_KEY = os.getenv("LIVE_API_SECRET")
    BASE_URL = os.getenv("LIVE_API_BASE_URL")
else:
    API_KEY = os.getenv("PAPER_API_KEY")
    SECRET_KEY = os.getenv("PAPER_API_SECRET")
    BASE_URL = os.getenv("PAPER_API_BASE_URL")

if not API_KEY or not SECRET_KEY or not BASE_URL:
    raise ValueError("❌ Missing API keys or base URL. Check .env settings.")

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

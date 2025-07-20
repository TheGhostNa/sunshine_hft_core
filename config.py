import os

from dotenv import load_dotenv

load_dotenv()

# ===========================
# 🔐 API KEYS
# ===========================

MODE = os.getenv("MODE", "paper")
SYMBOL = os.getenv("SYMBOL", "AAPL")
EQUITY = float(os.getenv("EQUITY", 10000))

if MODE == "live":
    APCA_API_KEY_ID = os.getenv("LIVE_API_KEY")
    APCA_API_SECRET_KEY = os.getenv("LIVE_API_SECRET")
    BASE_URL = os.getenv("LIVE_API_BASE_URL")
else:
    APCA_API_KEY_ID = os.getenv("PAPER_API_KEY")
    APCA_API_SECRET_KEY = os.getenv("PAPER_API_SECRET")
    BASE_URL = os.getenv("PAPER_API_BASE_URL")

# ===========================
# 🧠 TRADING SETTINGS
# ===========================
USE_PAPER_TRADING = MODE == "paper"
MAX_CAPITAL = EQUITY
TRADE_FRACTION = 0.05  # 5% of capital per trade

# ===========================
# 🔔 NOTIFICATION SETTINGS
# ===========================
TELEGRAM_NOTIFICATIONS = os.getenv("TELEGRAM_NOTIFICATIONS", "no") == "yes"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMAIL_NOTIFICATIONS = os.getenv("EMAIL_NOTIFICATIONS", "no") == "yes"
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# ===========================
# 🔗 DATA URL (Alpaca)
# ===========================
DATA_URL = "https://data.alpaca.markets/v2"

# ===========================
# 🔁 LOOP SETTINGS
# ===========================
INTERVAL = int(os.getenv("INTERVAL", 60))  # Loop interval in seconds

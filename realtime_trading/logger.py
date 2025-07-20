import logging
from logging.handlers import RotatingFileHandler

# Setup logger
logger = logging.getLogger("SunshineHFT")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler("sunshine_hft.log", maxBytes=5 * 1024 * 1024, backupCount=2)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


def log_info(msg):
    logger.info(msg)
    print(msg)  # Also print to console


def log_error(msg):
    logger.error(msg)
    print("ERROR:", msg)

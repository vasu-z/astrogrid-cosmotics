import datetime
import logging

logging.basicConfig(filename="app/logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")


def get_glow_color(expiry_date: str) -> str:
    expiry = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
    now = datetime.datetime.now()
    delta = (expiry - now).days

    if delta < 0:
        return "Red (Expired)"
    elif delta <= 5:
        return "Yellow (Expiring Soon)"
    else:
        return "Green (Safe)"


def log_action(action: str):
    logging.info(action)

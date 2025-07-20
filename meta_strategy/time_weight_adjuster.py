# meta_strategy/time_weight_adjuster.py

from datetime import datetime


def time_weight_adjust(base_weight: float) -> float:
    """
    Adjusts signal strength based on time of day.
    Example: Boost signal during opening and closing hours of market.
    """
    now = datetime.utcnow().hour

    # US market open: 13:30 UTC to 20:00 UTC (9:30am to 4:00pm EST)
    if 13 <= now <= 15:  # Opening hours boost
        return base_weight * 1.2
    elif 19 <= now <= 20:  # Closing hours boost
        return base_weight * 1.15
    else:  # Normal hours
        return base_weight

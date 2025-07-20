# meta_strategy/strategy_score_tracker.py

# Placeholder logic for now. We'll expand it later with actual tracking logic.
strategy_scores = {}


def update_strategy_score(symbol: str, strategy_name: str, result: str):
    """
    Update the score of a strategy for a given symbol.
    `result` can be 'win' or 'loss' (placeholder logic for now).
    """
    key = (symbol, strategy_name)
    if key not in strategy_scores:
        strategy_scores[key] = {"win": 0, "loss": 0}

    if result == "win":
        strategy_scores[key]["win"] += 1
    elif result == "loss":
        strategy_scores[key]["loss"] += 1


def get_strategy_scores():
    return strategy_scores

import os

import pandas as pd


class LogIntegrityChecker:
    def __init__(self, log_files):
        self.log_files = log_files  # dict {strategy_name: path}

    def validate_logs(self):
        errors = []
        required_columns = [
            "timestamp",
            "symbol",
            "action",
            "price",
            "quantity",
            "profit",
            "strategy",
        ]

        for name, path in self.log_files.items():
            if not os.path.exists(path):
                errors.append((name, "Missing File"))
                continue
            try:
                df = pd.read_csv(path)
                missing = [col for col in required_columns if col not in df.columns]
                if missing:
                    errors.append((name, f"Missing Columns: {missing}"))
            except Exception as e:
                errors.append((name, f"Corrupt File: {e}"))

        return errors

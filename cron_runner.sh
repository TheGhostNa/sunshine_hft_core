cd /path/to/sunshine_hft_core
source .venv/bin/activate
python -m dashboard.auto_report_runner

# Add this to crontab: (runs every 30 mins)
# */30 * * * * /path/to/cron_runner.sh


# ✅ USAGE COMMANDS:
# - Simulate trades:
python simulate_trades.py

# - Generate dashboard:
python -m dashboard.auto_report_runner

# - Filter logs by last 7 days:
from dashboard.time_range_filter import filter_log_by_days
filter_log_by_days("logs/rsi_trades.csv", 7)

# - Compare strategies:
from dashboard.strategy_comparator import compare_strategies
compare_strategies()

# - Validate logs manually:
python -m dashboard.log_validator_wrapper

# - Archive old logs:
python dashboard/cleaner.py

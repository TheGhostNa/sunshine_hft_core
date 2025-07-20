import os
import subprocess
from pathlib import Path

root_path = Path.cwd()

skip_dirs = {
    ".venv", "assets", "commands", "images", "includes", "javascripts", "overrides",
    "stylesheets", "backtest_results", "data", "freqaimodels", "hyperopts", "logs", "notebooks"
}

cleaned_files = []

for dirpath, dirnames, filenames in os.walk(root_path):
    if any(skip in Path(dirpath).parts for skip in skip_dirs):
        continue
    for filename in filenames:
        if filename.endswith(".py"):
            cleaned_files.append(str(Path(dirpath) / filename))

# Run flake8 in batches to avoid WinError 206
BATCH_SIZE = 50
for i in range(0, len(cleaned_files), BATCH_SIZE):
    batch = cleaned_files[i:i + BATCH_SIZE]
    subprocess.run(["flake8", *batch])

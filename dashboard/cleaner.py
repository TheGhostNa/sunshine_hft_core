import os
import shutil
from datetime import datetime

log_dir = "logs"
archive_dir = os.path.join(log_dir, "archived")
os.makedirs(archive_dir, exist_ok=True)

for file in os.listdir(log_dir):
    if file.endswith(".csv"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.move(os.path.join(log_dir, file), os.path.join(archive_dir, f"{timestamp}_{file}"))

print("✅ Logs archived.")

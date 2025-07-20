import os

import matplotlib.pyplot as plt
import pandas as pd

# Load trades
log_path = "logs/trades.csv"
if not os.path.exists(log_path):
    print("❌ Trade log not found. Run some trades first.")
    exit()

df = pd.read_csv(log_path)

# Ensure required columns exist
if not {"timestamp", "asset", "price", "side"}.issubset(df.columns):
    print("❌ Log format incorrect. Needs columns: timestamp, asset, price, side")
    exit()

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort by time
df = df.sort_values(by="timestamp")

# Create a simple PnL tracker
pnl_data = {}
for asset in df["asset"].unique():
    asset_df = df[df["asset"] == asset].copy()
    asset_df["pnl"] = 0.0
    position = 0
    entry_price = 0

    for i, row in asset_df.iterrows():
        price = row["price"]
        side = row["side"]

        if side == "BUY":
            if position == 0:
                entry_price = price
            position += 1
        elif side == "SELL" and position > 0:
            pnl = (price - entry_price) * position
            asset_df.at[i, "pnl"] = pnl
            position = 0  # reset after sell

    pnl_data[asset] = asset_df

# Plot
plt.figure(figsize=(12, 6))
for asset, data in pnl_data.items():
    data["cum_pnl"] = data["pnl"].cumsum()
    plt.plot(data["timestamp"], data["cum_pnl"], label=asset)

plt.title("📈 PnL Over Time (Simulated)")
plt.xlabel("Time")
plt.ylabel("Cumulative PnL ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd

df = pd.read_csv("data/AAPL_clean.csv")
print("📋 CSV Columns:")
print(df.columns.tolist())
print(df.head())

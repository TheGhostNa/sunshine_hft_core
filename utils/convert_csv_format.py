import pandas as pd


def convert_to_standard_format(input_path, output_path):
    # Read file and skip first two metadata rows
    df = pd.read_csv(input_path, skiprows=2)

    # Ensure only valid price rows are present
    df = df[df["Date"].notna()]  # Drop any rows where Date is NaN

    # Clean column names
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

    # Remove "Ticker" row if still present
    df = df[df["Date"] != "Ticker"]

    # Convert Date column to datetime format and set as index
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])  # Drop rows where Date couldn't be parsed
    df.set_index("Date", inplace=True)

    # Save to output
    df.to_csv(output_path)
    print(f"✅ Clean CSV saved at: {output_path}")
    print("📋 Final Columns:", df.columns.tolist())


if __name__ == "__main__":
    convert_to_standard_format("data/AAPL_historical.csv", "data/AAPL_clean.csv")

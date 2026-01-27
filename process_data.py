import pandas as pd
from pathlib import Path

# Paths
DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Read all CSV files in data folder
files = list(DATA_DIR.glob("*.csv"))

df_list = []
for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Keep only Pink Morsels
df = df[df["product"] == "Pink Morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Save output
output_file = OUTPUT_DIR / "pink_morsel_sales.csv"
df.to_csv(output_file, index=False)

print(f"Saved processed data to {output_file}")

import pandas as pd
from pathlib import Path

# Folder paths
data_folder = Path("data")
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

# Read all CSV files
all_files = data_folder.glob("*.csv")

dataframes = []

for file in all_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine all CSVs into one DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Keep only Pink Morsels
pink_df = combined_df[combined_df["product"] == "Pink Morsel"]

# Create Sales column
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Select required fields
final_df = pink_df[["Sales", "date", "region"]]

# Rename columns for clarity (optional but clean)
final_df.columns = ["Sales", "Date", "Region"]

# Save output
output_path = output_folder / "pink_morsel_sales.csv"
final_df.to_csv(output_path, index=False)

print("✅ Data processing complete!")
print(f"Output saved to {output_path}")

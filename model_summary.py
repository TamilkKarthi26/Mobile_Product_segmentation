import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_clustered.csv"
)

df = pd.read_csv(file_path)

mobile_df = (
    df.groupby(["brand", "model"])
      .agg({
          "price_usd":"mean",
          "rating":"mean",
          "battery_life_rating":"mean",
          "camera_rating":"mean",
          "performance_rating":"mean",
          "design_rating":"mean",
          "display_rating":"mean",
          "helpful_votes":"mean"
      })
      .reset_index()
)

print("Unique Mobiles:", len(mobile_df))

print("\nFirst 5 Mobiles:")
print(mobile_df.head())

output_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_summary.csv"
)

mobile_df.to_csv(output_path, index=False)

print("\nmobile_summary.csv saved successfully!")
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_reviews.csv"
)

df = pd.read_csv(file_path)

# Fill numerical missing values
df["price_usd"] = df["price_usd"].fillna(
    df["price_usd"].median()
)

df["rating"] = df["rating"].fillna(
    df["rating"].median()
)

# Fill categorical missing values
df["sentiment"] = df["sentiment"].fillna(
    "Neutral"
)

df["source"] = df["source"].fillna(
    "Unknown"
)

df["price_local"] = df["price_local"].fillna(
    "Unknown"
)

# Convert review date
df["review_date"] = pd.to_datetime(
    df["review_date"]
)

print("Missing Values After Cleaning:\n")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

# Save cleaned file
output_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_reviews_cleaned.csv"
)

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
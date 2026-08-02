import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_reviews_cleaned.csv"
)

df = pd.read_csv(file_path)

# Encode categorical columns
le_brand = LabelEncoder()
le_model = LabelEncoder()

df["brand_encoded"] = le_brand.fit_transform(df["brand"])
df["model_encoded"] = le_model.fit_transform(df["model"])

# Features for clustering
features = [
    "price_usd",
    "rating",
    "battery_life_rating",
    "camera_rating",
    "performance_rating",
    "design_rating",
    "display_rating",
    "helpful_votes"
]

X = df[features]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

df["cluster"] = kmeans.fit_predict(X_scaled)

print(df[["brand","model","price_usd","cluster"]].head())

print("\nCluster Counts:")
print(df["cluster"].value_counts())
cluster_summary = df.groupby("cluster")[
    [
        "price_usd",
        "rating",
        "battery_life_rating",
        "camera_rating",
        "performance_rating",
        "design_rating",
        "display_rating",
        "helpful_votes"
    ]
].mean()

print("\nCluster Summary:")
print(cluster_summary)
cluster_names = {
    0: "Mid-Range Phones",
    1: "Best Value Phones",
    2: "Low Satisfaction Phones",
    3: "Premium Flagships"
}

df["segment"] = df["cluster"].map(cluster_names)
print(df[["brand","model","segment"]].head())
import os

output_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_clustered.csv"
)

df.to_csv(output_path, index=False)

print("\nmobile_clustered.csv saved successfully!")
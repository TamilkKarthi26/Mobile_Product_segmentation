import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_dir,
    "..",
    "data",
    "mobile_summary.csv"
)

df = pd.read_csv(file_path)

features = [
    "price_usd",
    "rating",
    "battery_life_rating",
    "camera_rating",
    "performance_rating",
    "design_rating",
    "display_rating"
]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

similarity = cosine_similarity(X_scaled)

def recommend_mobile(model_name):

    idx = df[df["model"] == model_name].index[0]

    scores = list(enumerate(similarity[idx]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in scores[1:6]:
        recommendations.append(
            df.iloc[i[0]]["model"]
        )

    return recommendations

print("Recommendations for iPhone 14:\n")

print(recommend_mobile("iPhone 14"))
import streamlit as st
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Mobile Product Segmentation & Recommendation System",
    layout="wide"
)

# Load Data
df_reviews = pd.read_csv("data/mobile_reviews_cleaned.csv")
df_summary = pd.read_csv("data/mobile_summary.csv")
df_cluster = pd.read_csv("data/mobile_clustered.csv")

# Title
st.title("📱 Mobile Product Segmentation & Recommendation System")

# Sidebar
menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Dataset Overview",
        "EDA Insights",
        "Mobile Segmentation",
        "Recommendation System"
    ]
)

# Dataset Overview
if menu == "Dataset Overview":

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Reviews", len(df_reviews))

    with col2:
        st.metric("Total Brands", df_reviews["brand"].nunique())

    with col3:
        st.metric("Total Models", df_summary["model"].nunique())

    st.subheader("Sample Data")
    st.dataframe(df_reviews.head())

# EDA
elif menu == "EDA Insights":

    st.header("Exploratory Data Analysis")

    st.subheader("Brand Distribution")
    st.bar_chart(df_reviews["brand"].value_counts())

    st.subheader("Sentiment Distribution")
    st.bar_chart(df_reviews["sentiment"].value_counts())

    st.subheader("Country Distribution")
    st.bar_chart(df_reviews["country"].value_counts())

# Segmentation
elif menu == "Mobile Segmentation":

    st.header("Mobile Segmentation")

    segment_counts = df_cluster["segment"].value_counts()

    st.subheader("Segment Counts")
    st.bar_chart(segment_counts)

    st.subheader("Segment Distribution")

    st.write(segment_counts)

    st.subheader("Sample Segmented Data")

    st.dataframe(
        df_cluster[
            ["brand", "model", "rating", "segment"]
        ].head(20)
    )

# Recommendation
elif menu == "Recommendation System":

    st.header("Mobile Recommendation System")

    features = [
        "price_usd",
        "rating",
        "battery_life_rating",
        "camera_rating",
        "performance_rating",
        "design_rating",
        "display_rating"
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(
        df_summary[features]
    )

    similarity = cosine_similarity(X_scaled)

    mobile = st.selectbox(
        "Select Mobile",
        sorted(df_summary["model"].unique())
    )

    if st.button("Recommend"):

        idx = df_summary[
            df_summary["model"] == mobile
        ].index[0]

        scores = list(
            enumerate(similarity[idx])
        )

        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for i in scores[1:6]:

            recommendations.append(
                df_summary.iloc[i[0]][
                    [
                        "brand",
                        "model",
                        "price_usd",
                        "rating"
                    ]
                ]
            )

        result = pd.DataFrame(
            recommendations
        )

        st.subheader(
            f"Top 5 Recommendations for {mobile}"
        )

        st.dataframe(result)
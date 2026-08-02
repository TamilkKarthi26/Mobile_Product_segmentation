Mobile Product Segmentation and Recommendation System
Project Overview

This project analyzes mobile phone review data and builds a Machine Learning system to:

Clean and preprocess mobile review data
Perform Exploratory Data Analysis (EDA)
Segment mobile phones using K-Means Clustering
Recommend similar mobile phones using Cosine Similarity
Display insights through a Streamlit dashboard
Problem Statement

Customers often find it difficult to choose a suitable mobile phone from the large number of available options. This project groups similar mobile phones into segments and recommends alternative phones with similar characteristics.

Dataset Information
Total Records: 50,000
Total Features: 22
Brands Included: Apple, Samsung, Google, Xiaomi, OnePlus, Realme, Motorola, etc.
Data Includes:
Price
Rating
Battery Rating
Camera Rating
Performance Rating
Display Rating
Sentiment
Country
Review Information
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Project Workflow
Data Collection
Data Cleaning
Exploratory Data Analysis (EDA)
Feature Selection
K-Means Clustering
Mobile Segmentation
Recommendation System
Streamlit Dashboard
Machine Learning Models
K-Means Clustering

Used to group similar mobile phones into segments:

Best Value Phones
Mid-Range Phones
Premium Flagships
Low Satisfaction Phones
Recommendation System

Cosine Similarity is used to recommend similar mobile phones based on:

Price
Rating
Battery
Camera
Performance
Design
Display
Project Structure

Mobile_Product_Segmentation/

├── data/

├── notebooks/

├── src/

├── models/

├── app.py

├── README.md

└── requirements.txt

How to Run

Install dependencies:

pip install -r requirements.txt

Run Streamlit application:

streamlit run app.py

Results
Successfully segmented mobile phones into meaningful groups.
Built a recommendation system that suggests similar mobile phones.
Developed an interactive Streamlit dashboard for visualization and recommendations.
Conclusion

This project demonstrates how Machine Learning can be used to analyze mobile phone reviews, identify customer preferences, segment products, and provide personalized recommendations.

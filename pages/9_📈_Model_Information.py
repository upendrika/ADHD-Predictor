import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from PIL import Image
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import plotly.express as px



@st.cache_data
def load_data():
    df = pd.read_csv("ADHD.csv")
    return df

@st.cache_data
def get_fvalue(val):
    feature_dict = {"No": 1, "Yes": 2}
    return feature_dict.get(val, None)

def get_value(val, my_dict):
    return my_dict.get(val, None)
    


# Load your trained model (replace 'best_model.pkl' with your actual model file)
with open("best_random_forest_model.pkl", "rb") as f:
    best_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
    
# Category mapping (mapping numerical predictions to category names)
category_mapping = {0: "Unlikely", 1: "Likely", 2: "Highly Likely"}



# Feature columns (these should match the feature columns used during model training)
feature_columns = [
    "age", "sex", "Previous_state", "depression_Total", "Alcohol_total",
    "aas1_total", "University_Performance", "HighSchool_performance", 
    "Anexity_total", "aas_change"
]

st.sidebar.image('logo.png', width=180)

st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: darkblue;'>Model Information</h1>
</div>
""", unsafe_allow_html=True)

st.write("""
    The ADHD prediction model behind this app uses **machine learning classification techniques** to analyze various factors that may indicate ADHD symptoms.
""")

st.write("""
    By entering details about demographics, mental health, and academic performance, the app predicts the **ADHD category**. This prediction helps in identifying potential ADHD symptoms and understanding areas where intervention may be beneficial.
""")

st.markdown("""
<div>
    <h3 style='color: Black;'>Model Training Details</h3>
</div>
""", unsafe_allow_html=True)

st.subheader('Dataset')
st.write(
"""
The model was trained using a **publicly available dataset from Kaggle** focused on ADHD and mental health. 
The dataset includes detailed information on demographics, academic performance, and behavioral health indicators.
"""
)

# Adding a link to the dataset
st.markdown(
    "[Kaggle's ADHD and Mental Health Dataset](https://www.kaggle.com/datasets/xyz/adhd-mental-health)"
)

st.subheader('Algorithms Used')
st.write(
    """
    The model was built and optimized using the following **classification algorithms**:
    - **Logistic Regression**
    - **Decision Tree Classifier**
    - **Random Forest Classifier**
    - **Gradient Boosting Classifier**
    - **Support Vector Classifier (SVC)**
    """
)

st.subheader('Training Process')
st.write(
    """
    The dataset was split into **training** and **testing sets** to evaluate model performance. 
    **5-Fold Cross-Validation** was applied to ensure that the model generalizes well across different subsets of the data.
    """
)

st.subheader('Performance Evaluation')
st.write(
    """
    For a classification model, the following evaluation metrics were used to assess model performance:
    - **Accuracy**: Measures the overall correctness of the predictions.
    - **Precision**: Indicates the proportion of positive predictions that were actually correct.
    - **Recall (Sensitivity)**: Measures the ability to identify positive cases correctly.
    - **F1-Score**: Harmonic mean of precision and recall.
    - **ROC-AUC Score**: Represents the model's ability to distinguish between classes.
    """
)

st.image("evaluation.png", caption="Evaluation Metrics", width=500)
st.write(
    """
    The **Random Forest Classifier** was selected as the final model based on its **high accuracy, balanced precision, recall, and F1-score**.
    """
)

st.markdown("""
<div style='text-align: center;'>
    <h4>Model Insights and Takeaways</h4>
</div>
""", unsafe_allow_html=True)

st.write("""
    - The model demonstrated a strong ability to classify ADHD likelihood across different input scenarios.  
    - The **feature importance analysis** revealed key factors contributing to ADHD classification, including **anxiety levels, depression scores, and academic performance metrics**.  
    - The model is not a substitute for professional diagnosis but serves as a helpful tool for preliminary analysis.
""")


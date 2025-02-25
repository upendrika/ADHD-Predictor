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
    "aas1_total", "University_Performance", 
    "Anexity_total"
]

st.sidebar.image('logo.png', width=180)

st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: darkblue;'>Data Visualization</h1>
</div>
""", unsafe_allow_html=True)

# Load data
def load_data():
    df = pd.read_csv("ADHD.csv", encoding='latin1')  # Adjust encoding if needed
    return df

# Call the load_data function
df = load_data()

# Rename columns
df.rename(columns={
    'asrs1_total.y': 'adhd_total',
    
    'bdi1_total': 'depression_Total',
    'matric_mark': 'University_Performance',
    'bai1_total': 'Anexity_total',
    'audit1_total': 'Alcohol_total'
}, inplace=True)

# Create two columns for displaying graphs
col1, col2 = st.columns(2)

# Scatter Plot
with col1:
    st.markdown("<h3 style='font-size: 16px;'>Scatter Plot: ADHD Symptoms vs University Performance</h3>", unsafe_allow_html=True)
    fig1, ax1 = plt.subplots()
    ax1.scatter(df['adhd_total'], df['University_Performance'], alpha=0.5)
    ax1.set_title('ADHD Symptoms vs University Performance')
    ax1.set_xlabel('ADHD Total')
    ax1.set_ylabel('University Performance')
    st.pyplot(fig1)

# Violin Plot
with col2:
    st.markdown("<h3 style='font-size: 16px;'>Violin Plot: ADHD Symptoms across Depression Levels</h3>", unsafe_allow_html=True)
    
    df['depression_category'] = pd.cut(
        df['depression_Total'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High']
    )
    fig2, ax2 = plt.subplots()
    sns.violinplot(data=df, x='depression_category', y='adhd_total', palette='muted', ax=ax2)
    ax2.set_title('ADHD Symptoms across Depression Levels')
    ax2.set_xlabel('Depression Level')
    ax2.set_ylabel('ADHD Total')
    st.pyplot(fig2)

# Line Plot
with col1:
    st.markdown("<h3 style='font-size: 16px;'>Line Plot: ADHD Symptoms vs University Performance by Age</h3>", unsafe_allow_html=True)
    df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50], labels=['<20', '20-30', '30-40', '40-50'])
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=df, x='University_Performance', y='adhd_total', hue='age_group', markers=True, ax=ax3)
    ax3.set_title('ADHD Symptoms vs University Performance by Age')
    ax3.set_xlabel('University Performance')
    ax3.set_ylabel('ADHD Total Score')
    st.pyplot(fig3)

# Box Plot
with col2:
    st.markdown("<h3 style='font-size: 16px;'>Box Plot: Distribution of ADHD symptoms between different gender.</h3>", unsafe_allow_html=True)
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=df, x='sex', y='adhd_total', ax=ax4)
    ax4.set_title('ADHD Symptoms by Gender')
    ax4.set_xlabel('Gender')
    ax4.set_ylabel('ADHD Total')
    st.pyplot(fig4)

# Distribution Plot for aas_change 

    

# Correlation Heatmap
with col1:
    st.markdown("<h3 style='font-size: 16px;'>Correlation Heatmap: ADHD Symptoms and Other Variables</h3>", unsafe_allow_html=True)
    correlation_matrix = df[['adhd_total', 'University_Performance', 
                                'depression_Total', 'Anexity_total', 'Alcohol_total']].corr()
    fig7, ax7 = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax7)
    ax7.set_title('Correlation Heatmap of ADHD Symptoms and Other Variables')
    st.pyplot(fig7)



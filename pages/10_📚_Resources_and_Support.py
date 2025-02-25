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
    <h1 style='color: darkblue;'>Resources and Support</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div>
    <h3 style='color: Black;'>Managing ADHD in University Life</h3>
</div>
""", unsafe_allow_html=True)


st.write("""If you suspect that ADHD symptoms might be affecting your academic performance, you’re not alone. Here are some strategies and resources to help you thrive:
    """)

st.write("""
    - Time Management Tools: Use apps like Trello, Notion, or Google Calendar to organize tasks and set reminders.
    - Study Techniques: Break tasks into smaller, manageable parts and use the Pomodoro technique to stay focused.
    - Support Groups: Join university or online support groups for students with ADHD to share experiences and tips.
    - Mental Health Services: Reach out to your university’s counseling center for professional advice and support.
""")

st.markdown("""
<div>
    <h3 style='color: Black;'>Helpful Online Resources</h3>
</div>
""", unsafe_allow_html=True)


st.markdown("""
- <a href="https://chadd.org" target="_blank"><b>CHADD (Children and Adults with ADHD):</b></a> Provides educational resources, webinars, and support for individuals with ADHD.
- <a href="https://www.additudemag.com/" target="_blank"><b>ADDitude Magazine:</b></a> Offers expert advice on managing ADHD at school and beyond.
- <a href="https://www.adhdfoundation.org.uk/" target="_blank"><b>ADHD Foundation:</b></a> A charity providing resources and support for individuals with ADHD.
""", unsafe_allow_html=True)

st.markdown("""
<div>
    <h3 style='color: Black;'>Tips for Parents and Educators</h3>
</div>
""", unsafe_allow_html=True)
        
            
st.write("""
    - Foster a positive, encouraging environment.
    - Focus on strengths rather than just challenges.
    - Use visual aids and structured routines to support learning.

""")
             


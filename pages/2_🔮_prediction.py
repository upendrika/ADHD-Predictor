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
# Initialize session state for anxiety total if not present
if "anxiety_total" not in st.session_state:
    st.session_state.anxiety_total = 0  # Default value

def show_prediction():
    st.sidebar.image('logo.png', width=180)
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='color: darkblue;'>ADHD Category Predictor</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div>
            <h4 style='color: Black;'>We need some information to predict the ADHD category</h4>
        </div>
        """, unsafe_allow_html=True)

    
    
    with st.container():
        col_a, col_b = st.columns([2, 2])  # More space for input
        with col_a:
           age = st.number_input("Age", min_value=0, max_value=100, step=1)
        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            


    sex = st.radio("Sex", options=[0, 1, 2], 
                    format_func=lambda x: "Female" if x == 0 else "Male" if x == 1 else "Other")
    
    previous_state = st.radio("Previous State (0=No, 1=Yes)", options=[0, 1])
    

    with st.container():
        col_a, col_b = st.columns([2, 2])  # More space for input
        with col_a:
            depression_total = st.number_input("Depression Total", min_value=0, value=st.session_state.get("depression_total", 0))
        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Let's Find Your Depression Level"):
                st.switch_page("pages/3_📝_Depression_Form.py")

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        col_a, col_b = st.columns([2, 2])  # More space for input
        with col_a:
            alcohol_total = st.number_input("Alcohol Total", min_value=0, value=st.session_state.get("alcohol_total", 0))
        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Let's Find Your Alcohol Level"):
                st.switch_page("pages/4_📝_Alcohol_Form.py")

    st.markdown("<br>", unsafe_allow_html=True)


    with st.container():
        col_a, col_b = st.columns([2, 2])  # More space for input
        with col_a:
            aas1_total = st.number_input("AAS Total", min_value=0, value=st.session_state.get("aas1_total", 0))
        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Let's Find Your Academic Adjustment Scale"):
                st.switch_page("pages/5_📝_Academic_Adjustment_Form.py")


    st.markdown("<br>", unsafe_allow_html=True)

   

    
    # University Performance field
    with st.container():
        col_a, col_b = st.columns([2, 2])  # Adjust layout
        with col_a:
            # Get university performance, ensuring a default float value
            university_performance = st.session_state.get("university_performance", None)

            # Ensure the value is numeric; if not, default to 0.0
            if isinstance(university_performance, (int, float)):
                performance_value = university_performance
            else:
                performance_value = 0.0  # Default value

            university_performance = st.number_input(
                "University Performance (Grade)",
                value=performance_value,  # Use numeric value
                min_value=0.0, max_value=100.0, step=0.1
            )

        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Let's Select Your University Performance"):
                st.switch_page("pages/6_📝_University_Performance_Selection.py")  # Redirect to grade selection




    st.markdown("<br>", unsafe_allow_html=True)

    # Anxiety Total field should prefill with stored session value
    with st.container():
        col_a, col_b = st.columns([2, 2])  # More space for input
        with col_a:
            anxiety_total = st.number_input("Anxiety Total", min_value=0, value=st.session_state.get("anxiety_total", 0))
        with col_b:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Let's Find Your Anxiety Level"):
                st.switch_page("pages/7_📝_Anexity_Form.py")  # Navigate to the anxiety form

    st.markdown("<br>", unsafe_allow_html=True)
        
    category = None

    if st.button("Predict ADHD category"):
        try:
            # Prepare input data
            input_data = pd.DataFrame([[age, sex, previous_state, depression_total, alcohol_total,
                                        aas1_total, university_performance, anxiety_total]],
                                        columns=["age", "sex", "Previous_state", "depression_Total",
                                                "Alcohol_total", "aas1_total", "University_Performance",
                                                "Anexity_total"])

            # Scale input data
            input_data_scaled = scaler.transform(input_data)

            # Predict category
            adhd_category = best_model.predict(input_data_scaled)
            category = category_mapping.get(adhd_category[0], "Unknown")

        except Exception as e:
            st.error(f"Error: {e}")

    # Display Prediction Results
    st.markdown("---")  
    st.markdown("<h3 style='text-align: center; color: darkblue;'>Prediction Results</h3>", unsafe_allow_html=True)

    
    if category is not None:
        st.markdown(f"<h2 style='font-weight: bold; font-size: 24px;'>Predicted ADHD Category: {category}</h2>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        if category == "Highly Likely":
            st.error("High probability of ADHD symptoms detected. Consult a professional.")
            st.image("Highly Likely.png", caption="Take Action for Better Mental Health", use_container_width=True)
        elif category == "Likely":
            st.warning("Moderate probability of ADHD symptoms detected. Stay cautious and monitor regularly.")
            st.image("likely.png", caption="Stay Mindful and Seek Guidance", use_container_width=True)
        else:
            st.success("Unlikely to have ADHD symptoms. Keep maintaining a healthy routine.")
            st.image("Unlikely.png", caption="Keep Up the Good Work!", use_container_width=True)

    
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        - Category <span style="color:red; font-weight:bold;">'Highly Likely'</span>: ADHD total score ≥ 24.
        - Category <span style="color:orange; font-weight:bold;">'Likely'</span>: ADHD total score between 17 and 23.
        - Category <span style="color:green; font-weight:bold;">'Unlikely'</span>: ADHD total score between 0 and 16.
        """, unsafe_allow_html=True)


# Run the prediction page
if __name__ == "__main__":
    show_prediction()

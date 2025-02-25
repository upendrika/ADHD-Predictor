import streamlit as st

st.sidebar.image('logo.png', width=180)

st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: darkblue;'>Welcome to the <span style='color: red;'>ADHD</span> Prediction Tool for University Students</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div>
    <h3 style='color: Black;'>Purpose</h3>
</div>
""", unsafe_allow_html=True)

st.write("""
    This application provides a data-driven way for university students to assess ADHD symptoms. It analyzes behavioral,
    mental health, and academic factors to predict ADHD categories.
""")

st.markdown("""
<div>
    <h3 style='color: Black;'>What is <span style='color: red;'>ADHD</span>?</h3>
</div>
""", unsafe_allow_html=True)

st.write("""
    Attention Deficit Hyperactivity Disorder (ADHD) is a neurodevelopmental disorder characterized by inattention, hyperactivity,
    and impulsivity. Identifying ADHD early can help in managing these challenges and improving academic outcomes.
""")

st.subheader("Understanding and Supporting Students with ADHD")
st.video("Understanding and Supporting Your Student With ADHD.mp4")

st.markdown("""
<style>
video {
    height: 450px;
}
</style>
""", unsafe_allow_html=True)





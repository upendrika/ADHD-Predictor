import streamlit as st

st.sidebar.image('logo.png', width=180)

st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: darkblue;'>About</h1>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div>
    <h3 style='color: Black;'>The Motivation Behind This Application</h3>
</div>
""", unsafe_allow_html=True)

st.write("""
    This project stems from my individual research initiative aimed at understanding the impact of ADHD symptoms on university students’ academic performance. By combining insights from behavioral science and machine learning, I aim to provide a tool that helps students better understand and manage their mental well-being.
        """)



st.markdown("""
<div>
    <h3 style='color: Black;'>My Mission</h3>
</div>
""", unsafe_allow_html=True)

st.write("""
    My goal is to bridge the gap between awareness and action by making ADHD screening accessible, data-driven, and actionable. Ultimately, I hope to promote early identification and provide students with the resources needed to excel academically and personally.
            """)


st.markdown("""
<div>
    <h3 style='color: Black;'>Development</h3>
</div>
            
""", unsafe_allow_html=True)

st.write("""
    This app was developed as part of a my research project, leveraging publicly available data and machine learning techniques to create a reliable predictive model.
            """)


st.markdown("""
<div>
    <h3 style='color: Black;'>Acknowledgments </h3>
</div>
""", unsafe_allow_html=True)

st.write("""
    We would like to thank the educators, mental health professionals, and university students who contributed to this project, as well as the open data community for making this research possible. 
            """)

st.write("""
    - For more details about this project, feel free to contact me at isharaupendrika22@gmail.com.
""")


    # Your photo and introduction
col1, col2, col3 = st.columns([1, 1, 1])  # Center-align photo and details
with col3:
    st.image("ishara.jpeg", caption="Ishara Upendrika - Undergraduate", width=150)



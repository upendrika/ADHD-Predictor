import streamlit as st
st.sidebar.image('logo.png', width=180)
# Define the mapping for university performance
grade_mapping = {
    "A+": (90, 100), "A": (85, 89), "A-": (80, 84),
    "B+": (77, 79), "B": (73, 76), "B-": (70, 72),
    "C+": (67, 69), "C": (63, 66), "C-": (60, 62),
    "D+": (57, 59), "D": (53, 56), "D-": (50, 52),
    "F": (0, 49)
}

st.title("University Performance Selection")

# Dropdown for grade selection
selected_grade = st.selectbox("Select Your Grade", ["Not Selected"] + list(grade_mapping.keys()))

# Calculate and display the numeric average score
if selected_grade and selected_grade != "Not Selected":
    min_score, max_score = grade_mapping[selected_grade]
    avg_score = (min_score + max_score) / 2  # Take average of the range
    st.markdown(f"**Your Estimated Score:** {avg_score}")
else:
    avg_score = None  # No valid selection

# Submit button to save and redirect
if st.button("Submit and Return to Prediction Page"):
    if avg_score is not None:
        st.session_state.university_performance = avg_score  # Store numeric value
        st.success(f"University Performance saved: {avg_score}")
        st.switch_page("pages/2_🔮_prediction.py")  # Redirect to prediction page
    else:
        st.error("Please select a grade before proceeding.")

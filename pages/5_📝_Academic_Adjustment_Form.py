import streamlit as st 
st.sidebar.image('logo.png', width=180)
# Academic Adjustment Scale questions and response choices
aas1_questions = {
    "I am enjoying the lifestyle of being a university student.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I sometimes feel as though my education is not worth time away from my work or my family.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I sometimes worry I do not have the academic skills needed to enjoy being a student.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I am satisfied with the level of my academic performance to date.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I think I am as academically able as any other student.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I am satisfied with my ability to learn at university.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I expect to successfully complete my degree in the usual allocated timeframe.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "The reason I am studying is to lead to a better lifestyle.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ],
    "I will be disappointed if my studies don’t lead me to the career I want.": [
        "None", "Rarely applies to me", "Occasionally applies to me",
        "Neither does or doesn’t apply to me", "Sometimes applies to me", "Always applies to me"
    ]
}

# AAS scoring system
aas1_scores = {
    "None": 0, "Rarely applies to me": 1, "Occasionally applies to me": 2,
    "Neither does or doesn’t apply to me": 3, "Sometimes applies to me": 4, "Always applies to me": 5
}

# Function to calculate academic adjustment score
def get_aas1_score():
    st.title("Academic Adjustment Scale (AAS)")

    total_aas1_score = 0
    responses = {}

    # Loop through each question
    for question, options in aas1_questions.items():
        response = st.radio(question, options=options, key=question)
        
        # Assign score based on selected response
        score = aas1_scores[response]
        
        responses[question] = score
        total_aas1_score += score

    # Display total score
    st.markdown(f"### Total Academic Adjustment Score: {total_aas1_score}")
    return total_aas1_score


# Function to determine Academic Adjustment Level based on total score
def get_aas1_level(score):
    if score <= 12:
        return "Low Academic Adjustment"
    elif 13 <= score <= 24:
        return "Moderate Academic Adjustment"
    else:
        return "High Academic Adjustment"

# Main logic for AAS form
if __name__ == "__main__":
    if "aas1_total" not in st.session_state:
        st.session_state.aas1_total = 0  # Default value

    # Get AAS score based on responses
    total_score = get_aas1_score()

if total_score is not None:
    aas1_level = get_aas1_level(total_score)
    st.markdown(f"### Academic Adjustment Level: {aas1_level}")

    # Save the AAS score and navigate back
    if st.button("Submit and Return to Main Page"):
        st.session_state.aas1_total = total_score  # Store AAS total
        st.session_state.show_prediction_page = True  # Create navigation flag
        st.success(f"Academic Adjustment Score: {total_score} has been saved.")


    # Redirect back to the main prediction page
        st.switch_page("pages/2_🔮_prediction.py")  # Update this to your actual main prediction file

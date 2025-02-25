import streamlit as st 
st.sidebar.image('logo.png', width=180)
# Alcohol use assessment questions and answer choices
alcohol_questions = {
    "How often do you have a drink containing alcohol?": [
        "Never",
        "Monthly or less",
        "2 to 4 times a month",
        "2 to 3 times a week",
        "4 or more times a week"
    ],
    "How many drinks containing alcohol do you have on a typical day when you are drinking?": [
        "1 or 2",
        "3 or 4",
        "5 or 6",
        "7, 8, or 9",
        "10 or more"
    ],
    "How often do you have six or more drinks on one occasion?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "How often during the last year have you found that you were not able to stop drinking once you had started?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "How often during the last year have you failed to do what was normally expected from you because of drinking?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "How often during the last year have you needed a first drink in the morning to get yourself going after a heavy drinking session?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "How often during the last year have you had a feeling of guilt or remorse after drinking?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "How often during the last year have you been unable to remember what happened the night before because you had been drinking?": [
        "Never",
        "Less than monthly",
        "Monthly",
        "Weekly",
        "Daily or almost daily"
    ],
    "Have you or someone else been injured as a result of your drinking?": [
        "No",
        "Yes, but not in the last year",
        "Yes, during the last year"
    ],
    "Has a relative or friend or a doctor or another health worker been concerned about your drinking or suggested you cut down?": [
        "No",
        "Yes, but not in the last year",
        "Yes, during the last year"
    ]
}

# Alcohol scoring system
alcohol_scores = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4
}

# Function to calculate alcohol use score
def get_alcohol_score():
    st.title("Alcohol Use Assessment Form")

    total_alcohol_score = 0
    responses = {}

    # Loop through each question
    for index, (question, options) in enumerate(alcohol_questions.items()):
        response = st.radio(question, options=options, key=question)
        
        # Assign score based on selected response
        if index < 8:  # Questions 1-8 follow a 0-4 scoring
            score = options.index(response)
        else:  # Questions 9-10 have different scoring (0, 2, 4)
            score = [0, 2, 4][options.index(response)]
        
        responses[question] = score
        total_alcohol_score += score

    # Display total score
    st.markdown(f"### Total Alcohol Score: {total_alcohol_score}")
    return total_alcohol_score

# Determine alcohol use risk level based on score
def get_alcohol_risk_level(total_score):
    if total_score <= 7:
        return "Low risk"
    elif total_score <= 15:
        return "Moderate risk"
    elif total_score <= 19:
        return "High risk"
    else:
        return "Possible alcohol dependence"

# Main logic for alcohol form
if __name__ == "__main__":
    if "alcohol_total" not in st.session_state:
        st.session_state.alcohol_total = 0  # Default value

    # Get alcohol score based on responses
    total_score = get_alcohol_score()

    # Display alcohol use risk level
    if total_score is not None:
        alcohol_risk_level = get_alcohol_risk_level(total_score)
        st.markdown(f"### Alcohol Use Risk Level: {alcohol_risk_level}")

    # Save the alcohol score and navigate back
    if st.button("Submit and Return to Main Page"):
        st.session_state.alcohol_total = total_score  # Store alcohol total
        st.session_state.show_prediction_page = True  # Create navigation flag
        st.success(f"Alcohol Total Score: {total_score} has been saved.")

    # Redirect back to the main prediction page
        st.switch_page("pages/2_🔮_prediction.py")  # Update this to your actual main prediction file



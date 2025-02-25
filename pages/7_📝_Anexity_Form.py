import streamlit as st 
st.sidebar.image('logo.png', width=180)
# List of anxiety-related questions
questions = [
    "Numbness or tingling", "Feeling hot", "Wobbliness in legs", "Unable to relax",
    "Fear of worst happening", "Dizzy or lightheaded", "Heart pounding/racing", "Unsteady",
    "Terrified or afraid", "Nervous", "Feeling of choking", "Hands trembling", "Shaky / unsteady",
    "Fear of losing control", "Difficulty in breathing", "Fear of dying", "Scared", "Indigestion",
    "Faint / lightheaded", "Face flushed", "Hot/cold sweats"
]

# Possible answers for each question
answers = {
    "Not At All": 0,
    "Mildly but it didn’t bother me much": 1,
    "Moderately - it wasn’t pleasant at times": 2,
    "Severely – it bothered me a lot": 3
}

# Function to display the questionnaire and calculate total anxiety score
def get_anxiety_score():
    total_score = 0
    st.title("Anxiety Assessment Form")

    # Loop through the questions and collect responses
    responses = {}
    for question in questions:
        response = st.radio(question, options=list(answers.keys()), key=question)
        if response is not None:
            responses[question] = answers[response]
            total_score += answers[response]
        else:
            st.warning(f"Please answer all questions. You haven't answered '{question}'.")

    # Display the total anxiety score
    st.markdown(f"### Total Anxiety Score: {total_score}")
    return total_score

# Determine the anxiety level based on the total score
def get_anxiety_level(total_score):
    if total_score <= 21:
        return "Low Anxiety"
    elif total_score <= 35:
        return "Moderate Anxiety"
    else:
        return "Potentially Concerning Levels of Anxiety"

# Main logic for the anxiety form
if __name__ == "__main__":
    if "anxiety_total" not in st.session_state:
        st.session_state.anxiety_total = 0  # Default value

    # Get anxiety score based on responses
    total_score = get_anxiety_score()

    # After the user answers all questions, display the anxiety level
    if total_score is not None:
        anxiety_level = get_anxiety_level(total_score)
        st.markdown(f"### Anxiety Level: {anxiety_level}")

        
    if st.button("Submit and Return to Main Page"):
        st.session_state.anxiety_total = total_score  # Store the anxiety total
        st.success(f"Anxiety Total Score: {total_score} has been saved.")
        
        # Redirect back to the main prediction page
        st.switch_page("pages/2_🔮_prediction.py")  # Update this to your actual main prediction file

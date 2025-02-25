import streamlit as st 
st.sidebar.image('logo.png', width=180)
# List of depression-related questions and their answer choices
depression_questions = {
    "Sadness": ["I do not feel sad.", "I feel sad much of the time.", "I am sad all the time.", "I am so sad or unhappy that I can't stand it."],
    "Pessimism": ["I am not discouraged about my future.", "I feel more discouraged about my future than I used to.", "I do not expect things to work out for me.", "I feel my future is hopeless and will only get worse."],
    "Past Failure": ["I do not feel like a failure.", "I have failed more than I should have.", "As I look back, I see a lot of failures.", "I feel I am a total failure as a person."],
    "Loss of Pleasure": ["I get as much pleasure as I ever did from the things I enjoy.", "I don't enjoy things as much as I used to.", "I get very little pleasure from the things I used to enjoy.", "I can't get any pleasure from the things I used to enjoy."],
    "Guilty Feelings": ["I don't feel particularly guilty.", "I feel guilty over many things I have done or should have done.", "I feel quite guilty most of the time.", "I feel guilty all of the time."],
    "Punishment Feelings": ["I don't feel I am being punished.", "I feel I may be punished.", "I expect to be punished.", "I feel I am being punished."],
    "Self-Dislike": ["I feel the same about myself as ever.", "I have lost confidence in myself.", "I am disappointed in myself.", "I dislike myself."],
    "Self-Criticalness": ["I don't criticize or blame myself more than usual.", "I am more critical of myself than I used to be.", "I criticize myself for all of my faults.", "I blame myself for everything bad that happens."],
    "Suicidal Thoughts or Wishes": ["I don't have any thoughts of killing myself.", "I have thoughts of killing myself, but I would not carry them out.", "I would like to kill myself.", "I would kill myself if I had the chance."],
    "Crying": ["I don't cry anymore than I used to.", "I cry more than I used to.", "I cry over every little thing.", "I feel like crying, but I can't."],
    "Agitation": ["I am no more restless or wound up than usual.", "I feel more restless or wound up than usual.", "I am so restless or agitated, it's hard to stay still.", "I am so restless or agitated that I have to keep moving or doing something."],
    "Loss of Interest": ["I have not lost interest in other people or activities.", "I am less interested in other people or things than before.", "I have lost most of my interest in other people or things.", "It's hard to get interested in anything."],
    "Indecisiveness": ["I make decisions about as well as ever.", "I find it more difficult to make decisions than usual.", "I have much greater difficulty in making decisions than I used to.", "I have trouble making any decisions."],
    "Worthlessness": ["I do not feel I am worthless.", "I don't consider myself as worthwhile and useful as I used to.", "I feel more worthless as compared to others.", "I feel utterly worthless."],
    "Loss of Energy": ["I have as much energy as ever.", "I have less energy than I used to have.", "I don't have enough energy to do very much.", "I don't have enough energy to do anything."],
    "Changes in Sleeping Pattern": ["I have not experienced any change in my sleeping.", "I sleep somewhat more than usual.", "I sleep a lot more than usual.", "I sleep most of the day."],
    "Irritability": ["I am not more irritable than usual.", "I am more irritable than usual.", "I am much more irritable than usual.", "I am irritable all the time."],
    "Changes in Appetite": ["I have not experienced any change in my appetite.", "My appetite is somewhat less than usual.", "My appetite is much less than before.", "I have no appetite at all."],
    "Concentration Difficulty": ["I can concentrate as well as ever.", "I can't concentrate as well as usual.", "It's hard to keep my mind on anything for very long.", "I find I can't concentrate on anything."],
    "Tiredness or Fatigue": ["I am no more tired or fatigued than usual.", "I get more tired or fatigued more easily than usual.", "I am too tired or fatigued to do a lot of the things I used to do.", "I am too tired or fatigued to do most of the things I used to do."],
    "Loss of Interest in Sex": ["I have not noticed any recent change in my interest in sex.", "I am less interested in sex than I used to be.", "I am much less interested in sex now.", "I have lost interest in sex completely."]
}

# Depression answer scoring
depression_scores = {
    "0": 0, "1": 1, "2": 2, "3": 3
}

# Function to calculate depression score
def get_depression_score():
    st.title("Depression Assessment Form")
    
    total_depression_score = 0
    responses = {}

    # Loop through each question
    for question, options in depression_questions.items():
        response = st.radio(question, options=options, key=question)
        score = options.index(response)  # Assign score based on selected response
        responses[question] = score
        total_depression_score += score

    # Display total score
    st.markdown(f"### Total Depression Score: {total_depression_score}")
    return total_depression_score

# Determine depression level based on score
def get_depression_level(total_score):
    if total_score <= 21:
        return "Minimal or No Depression"
    elif total_score <= 35:
        return "Mild Depression"
    elif total_score <= 49:
        return "Moderate Depression"
    else:
        return "Severe Depression"

# Main logic for depression form
if __name__ == "__main__":
    if "depression_total" not in st.session_state:
        st.session_state.depression_total = 0  # Default value

    # Get depression score based on responses
    total_score = get_depression_score()

    # Display depression level
    if total_score is not None:
        depression_level = get_depression_level(total_score)
        st.markdown(f"### Depression Level: {depression_level}")

    # Save the depression score and navigate back
    if st.button("Submit and Return to Main Page"):
        st.session_state.depression_total = total_score  # Store depression total
        st.session_state.show_prediction_page = True  # Create navigation flag
        st.success(f"Depression Total Score: {total_score} has been saved.")


        st.switch_page("pages/2_🔮_prediction.py")  
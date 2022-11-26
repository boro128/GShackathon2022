import streamlit as st
from scripts import send_email


def run():
    score = st.session_state['score']
    time = st.session_state['quiz_total_time']
    longest_streak = st.session_state['longest_streak']
    
    minutes = int(time // 60)
    seconds = int(time % 60)

    final_score = round(score / max(seconds, 10) * 50, 2)

    st.header(f"Thank you for taking this quiz. Your final score is: {final_score}")
    st.write(f"Your longest streak was {longest_streak}")
    st.write(f"The quiz took you {minutes} {'minutes' if minutes != 1 else 'minute'} and {seconds} {'seconds' if seconds != 1 else 'second'}")

    st.write("If you want to take part in the lottery submit your email below! The better your score the higher chance to win you have.")

    email = st.text_input("Your email", "email@example.com")

    if st.button("Submit"):
        send_email(email)

    st.write("Chcesz z nami pogadać, a nie masz pomysłu jak zacząć, wylosuj pytanie")

    if st.button("Random Question"):
        st.session_state['curr_view'] = 'random_questions'
        st.experimental_rerun()

    if st.button("back to main page"):
        st.session_state['curr_view'] = 'init'
        st.experimental_rerun()

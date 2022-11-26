import streamlit as st
from scripts import send_email


def run():
    st.header("Thank you for taking this quiz")

    st.write("Jak chcesz wziąć udział w losowaniu, to daj mail")

    email = st.text_input("Your email", "email@example.com")

    if st.button("Submit"):
        send_email(email)

    st.write("Chcesz z nami pogadać, a nie masz pomysłu jak zacząć, wylosuj pytanie")

    if st.button("Random Question"):
        st.session_state['curr_view'] = 'random_questions'

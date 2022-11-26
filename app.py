import streamlit as st
from tabs import random_questions
from PIL import Image

from tabs import submit_email_view


image = Image.open('resources/logo.png')
st.image(image)
st.title("Welcome to Goldman Sachs")



def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        # kod do innych plików
        st.write("View 0")
        if st.button("go to question"):
            st.session_state['curr_view'] = 'quiz_tech'
            # st.experimental_rerun()
        if st.button("go to random questions"):
            st.session_state['curr_view'] = 'random_questions'
            st.experimental_rerun()


def handle_quiz_tech_view():
    if st.session_state['curr_view'] == 'quiz_tech':
        # kod do innych plików
        st.write(f"Question {st.session_state['question']}")
        if st.button("go to next"):
            st.session_state['question'] += 1
            if st.session_state['question'] == 11:
                st.session_state['curr_view'] = 'submit_email'
            st.experimental_rerun()


def handle_random_questions_viev():
    if st.session_state['curr_view'] == 'random_questions':
        random_questions.run()


def handle_submit_email_view():
    if st.session_state['curr_view'] == 'submit_email':
        submit_email_view.run()


def main():
    if st.session_state == {}:
        st.session_state = {'curr_view': 'init', 'question': 1}

    handle_init_view()
    handle_quiz_tech_view()
    handle_submit_email_view()
    handle_random_questions_viev()


if __name__ == '__main__':
    main()

import streamlit as st
from tabs import random_questions
from PIL import Image


image = Image.open('resources/logo.png')
st.image(image)
st.title("Welcome to Goldman Sachs")


def show_some_buttons():
    if st.button("asdfas"):
        st.write("fjas")


def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        # kod do innych plików
        st.write("View 0")
        show_some_buttons()
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
            # st.experimental_rerun()

def handle_random_questions_viev():
    if st.session_state['curr_view'] == 'random_questions':
        random_questions.run()
def handle_submit_email_view():
    pass


def main():
    if st.session_state == {}:
        st.session_state = {'curr_view': 'init', 'question': 1}

    handle_init_view()
    handle_quiz_tech_view()
    handle_submit_email_view()
    handle_random_questions_viev()



if __name__ == '__main__':
    main()

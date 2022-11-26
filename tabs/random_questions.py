import streamlit as st
import random
import os


@st.cache
def load_questions(path):
    with open(path, "r") as questions_file:
        questions = [question for question in questions_file]
        return questions


def run():
    questions = load_questions("data/questions.txt")
    st.markdown("## Here's a random question you can ask:")
    st.markdown(random.choice(questions))

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate New"):
            st.experimental_rerun()

    with col2:
        if st.button("Home Page"):
            st.session_state['curr_view'] = 'init'
            st.experimental_rerun()

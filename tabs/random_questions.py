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
    st.markdown("## here's a random question you can ask:")
    st.markdown(random.choice(questions))
    if st.button("generate new"):
        st.experimental_rerun()

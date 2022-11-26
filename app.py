import streamlit as st
from PIL import Image
import pandas as pd

from tabs import submit_email_view, random_questions, home


def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        home.run()


def handle_quiz_tech_view():
    if st.session_state['curr_view'] == 'quiz_tech':
        # kod do innych plików
        # st.write(f"Question {st.session_state['question']}")
        df = pd.read_csv("data/quiz.csv", header=0, sep=";")
        answers = st.radio(
            f"Question no {st.session_state['question']} \n {df.loc[st.session_state['question'], 'question']}",
            options=(df.loc[st.session_state['question'], 'odp1'], df.loc[st.session_state['question'], 'odp2'],
                     df.loc[st.session_state['question'], 'odp3'])
        )
        if st.button("go to next"):
            st.session_state['question'] += 1
            if st.session_state['question'] == 11:
                st.session_state['curr_view'] = 'submit_email'
            st.experimental_rerun()


def handle_random_questions_view():
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
    handle_random_questions_view()


if __name__ == '__main__':
    main()

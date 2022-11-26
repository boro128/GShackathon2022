import streamlit as st
import pandas as pd
import time


def score_answer(given_answer, correct_answer, is_final_question=False):
    if given_answer == correct_answer:
        st.session_state['score'] += 1
        st.session_state['streak'] += 1
    elif given_answer != correct_answer or is_final_question:
        st.session_state['score'] += st.session_state['streak']
        st.session_state['streak'] = 0


def run():
    df = pd.read_csv("data/quiz.csv", header=0, sep=";")

    question_idx = st.session_state['question']
    question_text = df.loc[question_idx, 'question']
    correct_answer = df.loc[question_idx, 'correct']

    given_answer = st.radio(
        f"Question no. {question_idx}\n{question_text}",
        options=(df.loc[st.session_state['question'], 'odp1'], 
                 df.loc[st.session_state['question'], 'odp2'],
                 df.loc[st.session_state['question'], 'odp3'])
    )

    if st.session_state['question'] == 1:
        st.session_state['score'] = 0

    if st.session_state['question'] >= 10:
        if st.button("finish_quiz"):
            score_answer(given_answer, correct_answer, is_final_question=True)
            st.session_state['streak'] = 0
            end_time = time.time()
            st.session_state['quiz_total_time'] = end_time - st.session_state['quiz_start_time']
            st.session_state['curr_view'] = 'submit_email'
            st.experimental_rerun()

    elif st.button("go to next"):
        score_answer(given_answer, correct_answer)
        st.session_state['question'] += 1
        st.experimental_rerun()

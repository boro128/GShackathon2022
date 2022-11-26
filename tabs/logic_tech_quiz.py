import streamlit as st
import pandas as pd
import time


def run():
    df = pd.read_csv("data/quiz.csv", header=0, sep=";")
    answers = st.radio(
        f"Question no {st.session_state['question']} \n {df.loc[st.session_state['question'], 'question']}",
        options=(df.loc[st.session_state['question'], 'odp1'], df.loc[st.session_state['question'], 'odp2'],
                 df.loc[st.session_state['question'], 'odp3'])
    )
    if st.session_state['question'] == 10:
        if st.button("finish_quiz"):
            end_time = time.time()
            st.session_state['quiz_total_time'] = end_time - st.session_state['quiz_start_time']
            st.session_state['curr_view'] = 'submit_email'
            st.experimental_rerun()
    elif st.button("go to next"):
        st.session_state['question'] += 1
        st.experimental_rerun()

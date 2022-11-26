import streamlit as st
import pandas as pd


def run():
    df = pd.read_csv("data/quiz.csv", header=0, sep=";")
    answers = st.radio(
        f"Question no {st.session_state['question']} \n {df.loc[st.session_state['question'], 'question']}",
        options=(df.loc[st.session_state['question'], 'odp1'], df.loc[st.session_state['question'], 'odp2'],
                 df.loc[st.session_state['question'], 'odp3'])
    )
    if st.session_state['question'] == 11:
        if st.button("finish_quiz"):
            st.session_state['curr_view'] = 'submit_email'
            st.experimental_rerun()

    if st.button("go to next"):
        st.session_state['question'] += 1
        st.experimental_rerun()

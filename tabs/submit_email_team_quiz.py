import streamlit as st
from tabs.utils import submit_mail_form


def calculate_team():
    data_analysis_ratio = 0
    devops_ratio = 0
    answers = st.session_state["team answers"]
    if answers[1][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[2][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[3][0]:
        devops_ratio += 1
    else:
        data_analysis_ratio += 1
    if answers[4][0]:
        devops_ratio += 1
    else:
        data_analysis_ratio += 1
    if answers[5][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[6][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[7][0] or answers[7][1]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if data_analysis_ratio > devops_ratio:
        st.write("")
    else:
        st.write("bardziej pasujesz do devopsa")


def show_team_1():
    st.markdown("zakon chleba")


def show_team_2():
    st.markdown("zakon bagietek")


def run():

    st.header(f"Thank you for taking this quiz.")

    st.write("Jak chcesz maila, to klik")

    submit_mail_form()

    st.write("If you would like to know more about us but you are not sure what to ask you can ask us a random question")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Random Question"):
            st.session_state['curr_view'] = 'random_questions'
            st.experimental_rerun()

    with col2:
        if st.button("Home Page"):
            st.session_state['curr_view'] = 'init'
            st.experimental_rerun()

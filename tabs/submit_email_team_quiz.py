import streamlit as st
from tabs.utils import submit_mail_form


def calculate_team():
    answers = st.session_state["team answers"]
    if answers[1][0]:
        show_team_1()
    else:
        show_team_2()


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

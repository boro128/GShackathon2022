import streamlit as st
import pandas as pd
import yaml


@st.cache
def load_questions(path):
    with open(path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


def show_team_1():
    st.markdown("Data Analysis Team")


def show_team_2():
    st.markdown("DevOps")


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

def run():
    questions = load_questions("data/team_quiz_questions.yaml")
    if st.session_state['team_question'] <= questions['num_questions']:
        curr_question = questions['questions'][st.session_state['team_question']]
        st.markdown(curr_question["text"])
        answer_list = []
        for answer in curr_question["answers"]:
            answer_list.append(st.checkbox(answer))
        if st.button("next question"):
            st.session_state["team answers"][st.session_state['team_question']] = answer_list
            st.session_state["team_question"] += 1
            st.experimental_rerun()
    else:
        calculate_team()
        if st.button("back to main page"):
            st.session_state['curr_view'] = 'init'
            st.session_state["team answers"] = {}
            st.session_state["team_question"] = 1
            st.experimental_rerun()

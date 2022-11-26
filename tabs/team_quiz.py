import streamlit as st
import yaml


@st.cache
def load_questions(path):
    with open(path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


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
        st.session_state['curr_view'] = 'submit_team_email'
        st.session_state["team_question"] = 1
        st.session_state['random_state'] += 1
        st.experimental_rerun()

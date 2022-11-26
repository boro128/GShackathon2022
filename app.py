import streamlit as st

from tabs import submit_email_tech_quiz, random_questions, home, logic_tech_quiz, team_quiz


def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        home.run()


def handle_quiz_tech_view():
    if st.session_state['curr_view'] == 'quiz_tech':
        logic_tech_quiz.run()


def handle_random_questions_view():
    if st.session_state['curr_view'] == 'random_questions':
        random_questions.run()


def handle_submit_email_view():
    if st.session_state['curr_view'] == 'submit_email':
        submit_email_tech_quiz.run()


def handle_team_quiz_view():
    if st.session_state['curr_view'] == 'team_quiz':
        team_quiz.run()


def main():
    if st.session_state == {}:
        st.session_state = {'curr_view': 'init',
                            'question': 1,
                            'quiz_start_time': -1,
                            'quiz_total_time': -1,
                            'score': 0,
                            'streak': 0,
                            'longest_streak': 0,
                            'team_question': 1,
                            'team answers': {}
                            }

    handle_init_view()
    handle_quiz_tech_view()
    handle_submit_email_view()
    handle_random_questions_view()
    handle_team_quiz_view()


if __name__ == '__main__':
    main()

import streamlit as st
from tabs import home

def show_some_buttons():
    if st.button("asdfas"):
        st.write("fjas")


def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        home.run()


def handle_questions_view():
    if st.session_state['curr_view'] == 'questions':
        # kod do innych plików
        st.write(f"Question {st.session_state['question']}")
        if st.button("go to next"):
            st.session_state['question'] += 1
            st.experimental_rerun()


def handle_submit_email_view():
    pass


def main():
    if st.session_state == {}:
        st.session_state = {'curr_view': 'init', 'question': 1}

    handle_init_view()
    handle_questions_view()
    handle_submit_email_view()


if __name__ == '__main__':
    main()

import streamlit as st
from PIL import Image
import pandas as pd

image = Image.open('resources/logo.png')
st.image(image)
st.title("Welcome to Goldman Sachs")
df = pd.read_csv("data/quiz.csv", header=0, sep=";")


def show_some_buttons():
    if st.button("asdfas"):
        st.write("fjas")


def handle_init_view():
    if st.session_state['curr_view'] == 'init':
        # kod do innych plików
        st.write("View 0")
        show_some_buttons()
        if st.button("go to question"):
            st.session_state['curr_view'] = 'questions'
            st.experimental_rerun()


def handle_questions_view():
    if st.session_state['curr_view'] == 'questions':
        # kod do innych plików
        # st.write(f"Question {st.session_state['question']}")
        answers = st.radio(
            f"Question no {st.session_state['question']} \n {df.loc[st.session_state['question'],'question']}",
            options=(df.loc[st.session_state['question'],'odp1'], df.loc[st.session_state['question'],'odp2'], df.loc[st.session_state['question'],'odp3'])
        )
        if st.button("go to next"):
            st.session_state['question'] += 1
            # st.experimental_rerun()


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

import streamlit as st
from PIL import Image


image = Image.open('resources/logo.png')
st.image(image)
st.title("Welcome to Goldman Sachs")

def show_some_buttons():
    if st.button("asdfas"):
        st.write("fjas")

if __name__ == '__main__':


    print()
    if st.session_state == {}:
        st.session_state = {'curr_view': 'init', 'question': 1}

    if st.session_state['curr_view'] == 'init':
        st.write("View 0")
        show_some_buttons()
        if st.button("go to question"):
            st.session_state['curr_view'] = 'questions'
            st.experimental_rerun()
            
    if st.session_state['curr_view'] == 'questions':
        st.write(f"Question {st.session_state['question']}")
        if st.button("go to next"):
            st.session_state['question'] += 1
            st.experimental_rerun()

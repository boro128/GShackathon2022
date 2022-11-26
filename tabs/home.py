import streamlit as st
import time
from PIL import Image


def run():
    
    image = Image.open('resources/logo.png')
    st.image(image)
    st.markdown("# Welcome to Goldman Sachs")    

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("If you would like to assess your skills and take part in our contest to win the grand prize...")
        if st.button("Take Tech Quiz"):
            st.session_state['curr_view'] = 'quiz_tech'
            st.session_state['quiz_start_time'] = time.time()
            st.experimental_rerun()

    with col2:
        st.markdown("If you want to see which of our teams suits you best and learn more about your potential position...")
        if st.button("Take Team Assessment Quiz"):
            st.session_state['curr_view'] = 'bread'
            st.experimental_rerun()

    with col3:
        st.markdown("If you want to learn more about us but you are not sure what to ask just...")
        if st.button("Ask us a random question!"):
            st.session_state['curr_view'] = 'random_questions'
            st.experimental_rerun()
    
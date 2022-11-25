import streamlit as st


def app():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Assess Your skills")
    with col2:
        st.button("Go", on_click=None)

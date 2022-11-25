import streamlit as st
from scripts import send_email

def run():
    st.write("QL wynik ziomek")

    email = st.text_input("Your email", "email@example.com")
    
    if st.button("Submit"):
        send_email(email)

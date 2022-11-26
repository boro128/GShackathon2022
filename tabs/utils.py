import streamlit as st
from email_validator import validate_email, EmailNotValidError
from scripts import send_email, save_mail_address


def check_mail(email):
    try:
        v = validate_email(email)
        return v["email"]
    except EmailNotValidError as e:
        st.error(str(e))
        return -1


def submit_mail_form():
    email = st.text_input("Your email", placeholder="email@example.com")

    if email != '':
        email = check_mail(email)

    submit_disabled = email == -1 or email == ''
    if st.button("Submit", disabled=submit_disabled):
        save_mail_address(email)
        send_email(email)
        st.success("Email send succesfully")

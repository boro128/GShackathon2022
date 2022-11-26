from redmail import outlook
from scripts.secrets import mail_password

# WYWALIĆ POTEM
import streamlit as st

# DODAĆ DO SECRETÓW
outlook.username = "czarny-lotos@outlook.com"
outlook.password = mail_password


def send_email(email: str):

    # WYWALIĆ POTEM
    if email != "czarny-lotos@outlook.com":
        st.write("Zmieniam mail na czarny-lotos@outlook.com")
        email = "czarny-lotos@outlook.com"

    outlook.send(
        subject="Test mail",
        receivers=[email],
        text="Test text")

import streamlit as st


def save_mail_address(path, email, final_score, time):
    with open(path, "a") as file:
        file.write(f"""{email};{final_score};{time}\n""")

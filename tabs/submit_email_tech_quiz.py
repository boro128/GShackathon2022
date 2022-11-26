import streamlit as st
from scripts import send_email
import pandas as pd
import plotly.express as px
from email_validator import validate_email, EmailNotValidError


def load_global_scores():
    data = pd.read_csv("data/scores.csv", sep=';', header=0)
    return data


def load_global_times():
    data = pd.read_csv("data/times.csv", sep=';', header=0)
    return data


def get_score_plot(data, new_score):
    color_discrete_sequence = ['#6b96c3']
    fig = px.bar(data, x='score', y='count', color_discrete_sequence=color_discrete_sequence)
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=100, b=100))
    fig.update_traces(width=2)
    fig.add_vline(x=new_score, line_color="#c38d6b")
    return fig

def get_time_plot(data, new_time):
    color_discrete_sequence = ['#6b96c3']
    fig = px.bar(data, x='time', y='count', color_discrete_sequence=color_discrete_sequence)
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=100, b=100))
    fig.update_traces(width=10)
    fig.add_vline(x=new_time, line_color="#c38d6b")
    return fig


def check_mail(email):
    try:
        v = validate_email(email)
        return v["email"]
    except EmailNotValidError as e:
        st.error(str(e))
        return -1


def run():
    score = st.session_state['score']
    time = st.session_state['quiz_total_time']
    longest_streak = st.session_state['longest_streak']

    minutes = int(time // 60)
    seconds = int(time % 60)

    final_score = round(score / max(seconds, 10) * 10, 2)

    st.header(f"Thank you for taking this quiz.")
    st.write(f"Your final score is: {final_score}")
    st.write(f"Your longest streak was {longest_streak} questions")
    st.write(
        f"The quiz took you {minutes} {'minutes' if minutes != 1 else 'minute'} and {seconds} {'seconds' if seconds != 1 else 'second'}")

    st.write("If you want to take part in the lottery submit your email below! The better your score the higher chance to win you have.")

    example_mail = "email@example.com"
    email = st.text_input("Your email", example_mail)
    if email != example_mail:
        email = check_mail(email)

    submit_disabled = email == -1 or email == example_mail
    if st.button("Submit", disabled=submit_disabled):
        send_email(email)

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(get_score_plot(load_global_scores(), final_score))
    with col2:
        st.plotly_chart(get_time_plot(load_global_times(), time))

    st.write("If you would like to know more about us but you are not sure what to ask you can ask us a random question")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Random Question"):
            st.session_state['curr_view'] = 'random_questions'
            st.experimental_rerun()

    with col2:
        if st.button("Home Page"):
            st.session_state['curr_view'] = 'init'
            st.experimental_rerun()

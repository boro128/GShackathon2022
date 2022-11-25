import streamlit as st
from pages import logic_tech_quiz
from multipage import MultiPage
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Welcome to Goldman Sachs")


app.add_page("Messages", logic_tech_quiz.app)


if __name__ == '__main__':
    app.run()

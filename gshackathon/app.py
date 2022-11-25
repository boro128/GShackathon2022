import streamlit as st
from pages import logic_tech_quiz, random_questions
from multipage import MultiPage
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Welcome to Goldman Sachs" + st.image())


app.add_page("Messages", logic_tech_quiz.app)
app.add_page("Random question", random_questions.app)

if __name__ == '__main__':
    app.run()

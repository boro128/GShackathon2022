import streamlit as st
from pages import logic_tech_quiz, random_questions
from multipage import MultiPage
from PIL import Image
# Create an instance of the app
app = MultiPage()
image = Image.open('resources/logo.png')
# Title of the main page
st.image(image)
st.title("Welcome to Goldman Sachs")


app.add_page("Messages", logic_tech_quiz.app)
app.add_page("Random question", random_questions.app)

if __name__ == '__main__':
    app.run()

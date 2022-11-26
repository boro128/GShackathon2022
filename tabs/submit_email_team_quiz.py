import streamlit as st
from tabs.utils import submit_mail_form
from PIL import Image

def calculate_team():
    data_analysis_ratio = 0
    devops_ratio = 0
    answers = st.session_state["team answers"]
    if answers[1][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[2][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[3][0]:
        devops_ratio += 1
    else:
        data_analysis_ratio += 1
    if answers[4][0]:
        devops_ratio += 1
    else:
        data_analysis_ratio += 1
    if answers[5][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[6][0]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    if answers[7][0] or answers[7][1]:
        data_analysis_ratio += 1
    else:
        devops_ratio += 1
    col1,col2 = st.columns(2)
    with col1:
        image = Image.open('resources/data_logo.png')
        image = image.resize((150,150))
        st.image(image)
        st.write(f"Fitted to Data Analysis Team: `{round(data_analysis_ratio/7, 2)}`")
        st.write("Data Analysis team take care about our Big Data problems, building predictive models, "
                 "doing analysis raports and data visualizations. Some of the technologies used there is: Python, R, Hadoop")
    with col2:
        image = Image.open('resources/devops_logo.png')
        image = image.resize((150, 150))
        st.image(image)
        st.write(f"\nFitted to DevOps Team: `{round(devops_ratio/7, 2)}`")
        st.write("Our DevOps team is in charge of "
                    "implementation the soutions build by our other teams. Some of the tools used in our DevOps team: "
                    "Jenkins, Docker, Kubernetes, Terraform")


def run():

    st.header(f"Thank you for taking this quiz.")
    calculate_team()
    st.write("If You want to hear more about job opportunities in Goldman Sachs leave us Your email")

    submit_mail_form()

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

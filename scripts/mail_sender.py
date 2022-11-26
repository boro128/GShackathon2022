from redmail import outlook
from scripts.secrets import mail_password, mail_login


outlook.username = mail_login
outlook.password = mail_password

EMAIL_TEMPLATE = """
<h1>Thank you for your interest in our company</h1>
<img src="{{ logo.src }}">
<br>
It was a pleasure to meet you during job fairs!
<br>
We encaurage you to check our <a href="https://www.goldmansachs.com/careers/students/programs/">open internship roles</a>.
"""


def send_email(email: str):

    # DELETE THIS LATER
    email = "czarny-lotos@outlook.com"

    outlook.send(
        subject="It was nice meeting you!",
        receivers=[email],
        html=EMAIL_TEMPLATE,
        body_images={
            'logo': 'resources/logo.png',
        }
    )

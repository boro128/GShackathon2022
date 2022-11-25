from redmail import outlook
from secrets import mail_password

outlook.username = "czarny-lotos@outlook.com"
outlook.password = mail_password

outlook.send(
    subject="Test mail",
    receivers=["czarny-lotos@outlook.com"],
    text="Test text"
)

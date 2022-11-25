from redmail import outlook

outlook.username = "czarny-lotos@outlook.com"
outlook.password = ""

outlook.send(
    subject="Test mail",
    receivers=["czarny-lotos@outlook.com"],
    text="Test text"
)

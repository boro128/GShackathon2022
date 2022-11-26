def save_mail_address(email):
    path = "data/mails.csv"
    with open(path, "a") as file:
        file.write(f"""{email}\n""")

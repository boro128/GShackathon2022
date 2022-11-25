import smtplib
# import ssl
port = 587  
smtp_server = "smtp-mail.outlook.com"
sender = "czarny-lotos@outlook.com"
recipient = "czarny-lotos@outlook.com"
sender_password = ""
message = """
Subject: This is a test message
Send using Python."""
# SSL_context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=SSL_context) as server:
with smtplib.SMTP(smtp_server, port) as server:

    server.ehlo()
    server.starttls()
    server.login(sender, sender_password)
    server.sendmail(sender, recipient, message)
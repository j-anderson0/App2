import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "seraphj51@gmail.com"
password = "ovnf lgov qwis xzvd"

receiver = "j.anderson822@gmail.com"
context = ssl.create_default_context()

message = """Subject: Python emailing test
Holla 'atcha boy!

The path forward is only forward and upward, my friend.

Sincerely,

J
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
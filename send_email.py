import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "iliadi.lo.lolita@gmail.com"
password = "voaaiorokinjpraf"

receiver = "iliadi.lo.lolita@gmail.com"
my_context = ssl.create_default_context()
message = '''\
Subject: It's me
Hi!
How are you?
'''

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
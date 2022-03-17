import smtplib, ssl
from dotenv import dotenv_values

smtp_server = "smtp.mail.yahoo.com"
 
port = 587  # For starttls

configs = dotenv_values('.env')

sender_email = configs['ADDRESS']
password = configs['PASSWORD']

context = ssl.create_default_context()

receiver_email = configs['TO'] 

message = """\
Subject: Hi there

This message is sent from Python."""

try:
    breakpoint()
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context) # Secure the connection
    print('authenticating...')
    server.login(sender_email, password)
    print('sending...')
    server.sendmail(sender_email, receiver_email, message)
    print('done...')
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

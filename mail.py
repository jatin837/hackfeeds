import smtplib, ssl
from dotenv import dotenv_values

def send(msg: str) -> None:
    with open('email', 'r') as f:
        e_addrs = f.read().strip().split('\n')
    smtp_server = "smtp.mail.yahoo.com"
    port = 587  # For starttls
    configs = dotenv_values('.env')
    sender_email = configs['ADDRESS']
    password = configs['PASSWORD']
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.set_debuglevel(1)
        server.starttls(context=context) # Secure the connection
        print('authenticating...')
        server.login(sender_email, password)
        print('sending...')
        for i, receiver_email in enumerate(e_addrs):
            server.sendmail(sender_email, receiver_email, msg=msg)
            print(f'{i} done...')
    except Exception as e:
        print(e)
    finally:
        server.quit() 

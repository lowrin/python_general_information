import smtplib
from email.mime.text import MIMEText


def sendMail(sender,receiver,password,subject,body):

    # for gmail with 2 factor authentification, use an app specific password, which could be created here:
    # https://security.google.com/settings/security/apppasswords

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


sendMail(sender="from",receiver="to",password="pwd",subject="subject",body="body")

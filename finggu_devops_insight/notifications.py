import os
import smtplib
from email.mime.text import MIMEText


def finggu_send_alert(subject, message):
    sender = os.getenv('FINGGU_EMAIL_SENDER')
    recipient = os.getenv('FINGGU_EMAIL_RECIPIENT')
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP(os.getenv('FINGGU_SMTP_SERVER'), int(os.getenv('FINGGU_SMTP_PORT'))) as server:
        server.starttls()
        server.login(sender, os.getenv('FINGGU_EMAIL_PASSWORD'))
        server.sendmail(sender, recipient, msg.as_string())
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import settings


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'efga49154@gmail.com'
smtp_password = 'Benney@1960'
sender = 'efga49154@gmail.com'


def change_password():
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)

        
        
        recipient = 'njeru.online.work@gmail.com'
        subject = 'Test Email'
        body = 'This is a test email message.'

        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send the email message
        smtp.send_message(message)


change_password()
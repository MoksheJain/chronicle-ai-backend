import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import SENDER_EMAIL, EMAIL_PASSWORD
from tools.sheet_manager import get_all_subscribers

def load_subscribers():
    return get_all_subscribers()


def send_newsletter(subject, html_content):
    subsribers = ["jainmokshejain2005@gmail.com"]
    for email in subsribers:
        msg = MIMEMultipart("alternative")
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = subject

        msg.attach(MIMEText(html_content, "html"))

        print("mail sent")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
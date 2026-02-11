import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import SENDER_EMAIL, EMAIL_PASSWORD
from tools.sheet_manager import get_all_subscribers

def load_subscribers():
    return get_all_subscribers()

def send_welcome_email(recipient_email):

    subject = "🎉 Welcome to ChronicleAI!"

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #0f172a; color: white; padding: 20px;">
        <h2>Welcome to ChronicleAI 📰</h2>
        <p>Thank you for subscribing!</p>
        <p>You’ll now receive AI-curated daily news summaries directly in your inbox.</p>
        <p><strong>Delivery Time:</strong> 9 AM daily</p>
        <br>
        <p>Stay informed. Stay ahead.</p>
        <br>
        <p>— The ChronicleAI Team</p>
    </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())


def send_newsletter(subject, html_content):
    subsribers = load_subscribers()
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
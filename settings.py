import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
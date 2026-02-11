from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from tools.sheet_manager import add_subscriber
from tools.email_sender import send_welcome_email

app = FastAPI()

class Subscriber(BaseModel):
    email: EmailStr   # automatic email validation

@app.post("/subscribe")
def subscribe(subscriber: Subscriber):

    try:
        # 1. Add to Google Sheet
        add_subscriber(subscriber.email)

        # 2. Send Welcome Email
        send_welcome_email(subscriber.email)

        return {"message": "Subscribed successfully. Check your email!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

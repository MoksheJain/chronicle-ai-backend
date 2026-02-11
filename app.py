from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from tools.sheet_manager import add_subscriber
from tools.email_sender import send_welcome_email
from fastapi.middleware.cors import CORSMiddleware
import traceback

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Subscriber(BaseModel):
    email: EmailStr   # automatic email validation


@app.post("/subscribe")
def subscribe(subscriber: Subscriber):

    try:
        add_subscriber(subscriber.email)
        send_welcome_email(subscriber.email)

        return {"message": "Subscribed successfully"}

    except Exception as e:
        print("ERROR OCCURRED:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI
from pydantic import BaseModel
from tools.sheet_manager import add_subscriber

app = FastAPI()

class Subscriber(BaseModel):
    email: str

@app.post("/subscribe")
def subscribe(subscriber: Subscriber):

    add_subscriber(subscriber.email)

    return {"message": "Subscribed successfully"}

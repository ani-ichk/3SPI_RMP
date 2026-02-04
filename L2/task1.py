from fastapi import FastAPI
from models import User


users = [
    User(name="John Doe", id=1)
]

app = FastAPI()

@app.get("/users")
def return_information():
    return users
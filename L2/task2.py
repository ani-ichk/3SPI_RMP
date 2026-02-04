from fastapi import FastAPI
from models import User2


app = FastAPI()


@app.post("/user")
def check_is_adult(user: User2):
    return {
        "name": user.name,
        "age":  user.age,
        "is_adult": user.age >= 18
    }
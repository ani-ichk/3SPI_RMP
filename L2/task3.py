from fastapi import FastAPI
from models import Feedback


app = FastAPI()

feedbacks = []


@app.post("/feedback")
def get_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
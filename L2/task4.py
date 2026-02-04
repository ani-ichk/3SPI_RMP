from fastapi import FastAPI
from models import Feedback2


app = FastAPI()

feedbacks = []

@app.post("/feedback")
def get_feedback(feedback: Feedback2):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
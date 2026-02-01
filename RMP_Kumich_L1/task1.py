from fastapi import FastAPI


aapp = FastAPI()

@aapp.get("/")
def task_1():
    return {"message": "Авторелоад действительно работает"}
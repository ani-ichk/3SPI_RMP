from fastapi import FastAPI


app = FastAPI()

@app.post("/calculate")
def calculate(num1: int, num2: int):
    return {"result": num1 + num2}
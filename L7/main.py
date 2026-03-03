import uvicorn
from fastapi import FastAPI
from api.router import router as api_router

app = FastAPI(title="Books")
app.include_router(api_router)

@app.get("/")
def read_root():
    return {
        "docs": "/docs",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
import uvicorn
from fastapi import FastAPI

from applifespan import lifespan
from rest.main_views import router as api_router


app = FastAPI(
    title='Books',
    lifespan=lifespan,
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
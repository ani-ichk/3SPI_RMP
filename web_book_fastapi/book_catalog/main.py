import uvicorn
from fastapi import FastAPI
from web_book_fastapi.book_catalog.api.main_views import router as api_router


app = FastAPI(title='Books')

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
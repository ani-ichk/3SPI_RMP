import uvicorn
from fastapi import FastAPI, APIRouter

from applifespan import lifespan
from rest.main_views import router as rest_router
from web_book_fastapi.book_catalog.api.api_v1.books.views.list_views import router as list_router
from web_book_fastapi.book_catalog.api.api_v1.books.views.details_views import router as details_router


api_router = APIRouter(prefix="/api/v1")
api_router.include_router(list_router)
api_router.include_router(details_router)

app = FastAPI(title='Books', lifespan=lifespan)

app.include_router(rest_router)
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
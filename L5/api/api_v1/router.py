from fastapi import APIRouter
from api.api_v1.books.views import router as books_router
from api.api_v1.movies.router import router as movies_router


router = APIRouter()
router.include_router(books_router)
router.include_router(movies_router)
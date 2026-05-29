from fastapi import APIRouter
from rest.main_views import router as main_views_router
from rest.books import router as books_router


router = APIRouter()
router.include_router(main_views_router)
router.include_router(books_router)
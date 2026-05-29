from fastapi import APIRouter
from rest.books.list_views import router as list_views_router


router = APIRouter(
    prefix="/books",
)

router.include_router(list_views_router)
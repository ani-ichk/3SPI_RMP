from fastapi import APIRouter
from api.api_v1.movies.list_views import router as list_router
from api.api_v1.movies.details_views import router as details_router


router = APIRouter()
router.include_router(list_router)
router.include_router(details_router)
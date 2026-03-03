from fastapi import APIRouter
from api.api_v1.movies.router import router as movies_router


router = APIRouter()
router.include_router(movies_router)
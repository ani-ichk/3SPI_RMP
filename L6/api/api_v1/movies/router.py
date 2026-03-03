from fastapi import APIRouter, Depends, status
from api.api_v1.movies.list_views import router as list_router
from api.api_v1.movies.details_views import router as details_router
from api.api_v1.movies.dependencies import verify_api_token



router = APIRouter(
    dependencies=[Depends(verify_api_token)],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "invalid token",
        },
    }
)
router.include_router(list_router)
router.include_router(details_router)
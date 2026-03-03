from fastapi import APIRouter
from api.api_v1.router import router as router_v1


router = APIRouter(prefix="/api")
router.include_router(router_v1, prefix="/v1")
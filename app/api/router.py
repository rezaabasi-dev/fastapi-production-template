from fastapi import APIRouter
from app.api.v1.users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/api/v1")

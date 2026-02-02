from .user.v1.router import router as user_v1_router
from fastapi import APIRouter


router = APIRouter()

router.include_router(user_v1_router)

__all__=["router"]
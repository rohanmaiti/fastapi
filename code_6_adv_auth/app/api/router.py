from fastapi import APIRouter
from app.api.auth.router import router as auth_router
from app.api.users.router import router as user_router


router = APIRouter(prefix="/api")

router.include_router(auth_router)
router.include_router(user_router)


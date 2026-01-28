from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter("/v1/user")

content={"status": "healthy", "service": "api helath checkup"}

@router.get("/health")
def root_router():
    response = JSONResponse(
        status_code=200,
        content=content
    )
    response.set_cookie(key="X-custom", value="admin123")
    return response 

 
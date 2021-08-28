from fastapi import Request, Query, APIRouter

from models import Stats
from routes.v1 import rate_limiter

users_router = APIRouter()

@users_router.get("/{uid}/stats")
async def route_user_stat(request: Request, uid: int):
    return Stats(uid=uid)

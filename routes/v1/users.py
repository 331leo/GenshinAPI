from fastapi import APIRouter, Query, Request

from models import Stats
from utils import get_user_stat

users_router = APIRouter()


@users_router.get(
    "/{uid}/stats",
    response_model=Stats,
    summary="Get In-game progress information with uid",
)
async def route_user_stat(
    request: Request,
    uid: int = Query(None, description="In-Game User Id", example=838687127),
):
    return await get_user_stat(uid)

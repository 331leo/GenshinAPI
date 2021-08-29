from typing import List

from fastapi import APIRouter, Depends, Query, Request, status
from genshinstats.errors import AccountNotFound, DataNotPublic, NotLoggedIn
from starlette.responses import JSONResponse, Response

from models import Character, Lang, Stats, UIDErrorModel
from models.exception import UIDErrorCode
from utils import get_user_stat
from utils.genshin import get_user_chracters

users_router = APIRouter(responses={"404": {"model": UIDErrorModel}})


@users_router.get(
    "/{uid}/stats",
    response_model=Stats,
    summary="Get In-game progress information with uid",
    response_description="Returns a JSON object with the user's game progress.",
)
async def route_user_stat(
    request: Request,
    uid: int = Query(838687127, title="In-Game User Id", example=838687127),
):
    return await get_user_stat(uid)


@users_router.get(
    "/{uid}/characters",
    response_model=List[Character],
    summary="Get all user's character info",
    description="Response language could be changed by _lang_ parameters",
    response_description="Returns a JSON object with the user's characters.",
)
async def route_user_characters(request: Request, uid: int, lang: Lang = Lang.ko_kr):
    return await get_user_chracters(uid, lang)

    # return JSONResponse(status_code=400, content={"message": "Not Implemented"})

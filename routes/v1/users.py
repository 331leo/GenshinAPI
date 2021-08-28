from fastapi import APIRouter, Query, Request, status
from genshinstats.errors import AccountNotFound, DataNotPublic, NotLoggedIn
from starlette.responses import JSONResponse, Response

from models import Stats, UIDErrorModel
from utils import get_user_stat

users_router = APIRouter(responses={"404": {"model": UIDErrorModel}})


@users_router.get(
    "/{uid}/stats",
    response_model=Stats,
    summary="Get In-game progress information with uid",
    response_description="Returns a JSON object with the user's game progress.",
)
async def route_user_stat(
    request: Request,
    uid: int = Query(None, description="In-Game User Id", example=838687127),
):
    try:
        return await get_user_stat(uid)
    except DataNotPublic:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"code": "PRIVATE", "message": "User profile is private."},
        )
    except AccountNotFound:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"code": "NON_EXISTING", "message": "UID does not exist."},
        )
    except NotLoggedIn:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"code": "NON_EXISTING", "message": "UID does not exist."},
        )

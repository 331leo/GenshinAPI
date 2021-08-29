from enum import Enum
from genshinstats.errors import DataNotPublic

from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND


class UIDErrorCode(str, Enum):
    PRIVATE = "PRIVATE"
    NONEXISTING = "NON_EXISTING"


def UIDExceptionHandler(request: Request, exc: Exception):
    if isinstance(exc, DataNotPublic):
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"code": UIDErrorCode.PRIVATE, "message": "User profile is private"})
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"code": UIDErrorCode.PRIVATE, "message": "UID does not exist"})


class UIDErrorModel(BaseModel):
    code: UIDErrorCode
    message: str

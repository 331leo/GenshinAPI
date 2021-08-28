from enum import Enum

from pydantic import BaseModel


class UIDErrorCode(str, Enum):
    PRIVATE = "PRIVATE"
    NONEXISTING = "NON_EXISTING"


class UIDErrorModel(BaseModel):
    code: UIDErrorCode
    message: str

from pydantic import BaseModel, StrictStr
from typing import List


class DeleteUserResponseSuccess(BaseModel):
    code: int


class DeleteUserResponseError(BaseModel):
    code: int
    message: StrictStr

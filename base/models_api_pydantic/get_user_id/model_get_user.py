from pydantic import BaseModel, StrictStr
from typing import List


class GetUserResponseSuccess(BaseModel):
    userID: StrictStr
    username: StrictStr
    books: List[str]


class GetUserResponseError(BaseModel):
    code: int
    message: StrictStr

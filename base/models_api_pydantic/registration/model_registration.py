from pydantic import BaseModel, StrictStr
from typing import List


class RegistrationResponseSuccess(BaseModel):
    userID: StrictStr
    username: StrictStr
    books: List[str]


class RegistrationResponseError(BaseModel):
    code: int
    message: StrictStr

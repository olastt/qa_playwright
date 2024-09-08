from pydantic import BaseModel, StrictStr
from typing import List


class RegistrationResponseSuccess(BaseModel):
    userID: StrictStr
    username: StrictStr
    books: List[str]   # Можно указать конкретный тип, если он известен


class RegistrationResponseError(BaseModel):
    code: int  # StrictInt можно заменить на обычный int
    message: StrictStr

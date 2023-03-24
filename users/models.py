from pydantic import BaseModel
from jwtdown_fastapi.authentication import Token
from datetime import datetime
from typing import Optional

class Error(BaseModel):
    message: str

class DuplicateUserError(ValueError):
    pass

class HttpError(BaseModel):
    detail: str

class UserForm(BaseModel):
    username: str
    password: str

class UserIn(BaseModel):
    email: str
    password: str
    pickup_name: str
    phone_number: str
    venmo: Optional[str]

class LoginForm(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    pickup_name: str
    phone_number: str
    venmo: str
    role: Optional[str]
    hashed_password: str

class UserToken(Token):
    user: UserOut

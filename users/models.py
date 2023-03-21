from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Error(BaseModel):
    message: str

class UserIn(BaseModel):
    name: str
    email: str
    phone_number: str
    venmo: Optional(str)
    role: Optional(str)
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    venmo: Optional(str)
    role: Optional(str)
    created_at: datetime
    password_last_modified: Optional(datetime)

class LoginForm(BaseModel):
    email: str
    password: str

class UserOutWithHashed(BaseModel):
    id: int
    email: str
    hashed_password: str

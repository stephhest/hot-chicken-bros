from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response
)
from models import (
    UserIn,
    LoginForm,
    UserOut,
    Error,
    HttpError,
    UserToken,
)
from authenticator import authenticator
from typing import List, Union
from queries.users import UserQueries


router = APIRouter()


@router.get("/token", response_model=Union[UserToken, None])
async def get_token(
    request: Request,
    user: dict = Depends(authenticator.try_get_current_account_data),
):
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }

@router.post("/api/users", response_model=Union[UserToken, HttpError])
async def create_user(
    input: UserIn,
    request: Request,
    response: Response,
    repo: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(input.password)
    user = repo.create(input, hashed_password)
    form = LoginForm(username=input.email, password=input.password)
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=user, **token.dict())

@router.get("/api/users/current", response_model=Union[dict, None])
def get_current_user(
    user: dict = Depends(authenticator.get_current_account_data),
):
    return user

@router.get("/api/users", response_model=Union[List[UserOut], Error])
def get_users(repo: UserQueries = Depends()):
    return repo.get_all()

@router.put("/api/users/current", response_model=Union[bool, Error])
def update_user(
    input: UserIn,
    user: dict = Depends(authenticator.get_current_account_data),
    repo: UserQueries = Depends()
):
    if user:
        user_id = user["id"]
        hashed_password = authenticator.hash_password(input.password)
        return repo.update(user_id, input, hashed_password)


@router.delete("/api/users/current", response_model=Union[bool, Error])
def delete_user(
    user: dict = Depends(authenticator.get_current_account_data),
    repo: UserQueries = Depends()
):
    if user:
        user_id = user["id"]
        return repo.delete(user_id)

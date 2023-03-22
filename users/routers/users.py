from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
    Response
)
from models import (
    UserIn,
    LoginForm,
    UserOut,
    UserOutWithPassword,
    Error,
    HttpError,
    DuplicateUserError,
    UserToken,
)
from authenticator import authenticator
from typing import List, Union, Optional
from queries.users import UserQueries


router = APIRouter()


@router.post("api/users", response_model=Union[UserToken, HttpError])
async def create_user(
    input: UserIn,
    request: Request,
    response: Response,
    repo: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(input.password)
    try:
        user = repo.create(input, hashed_password)
    except DuplicateUserError as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    form = LoginForm(email=input.email, password=input.password)
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=user, **token.dict())


@router.get("/api/users/current", response_model=UserOut)
def get_user_by_info(
    user: UserOut = Depends(authenticator.get_current_account_data),
):
    return user


@router.put("/api/users/current", response_model=UserOut)
def update_user():
    pass


def delete_user():
    pass

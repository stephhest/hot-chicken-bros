import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from datetime import timedelta
from queries.users import UserQueries
from models import UserOut


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        email: str,
        repo: UserQueries,
    ):
        # Use your repo to get the user based on email
        return repo.get(email)

    def get_account_getter(
        self,
        repo: UserQueries = Depends()
    ):
        # Return the repo. That's it.
        return repo

    def get_hashed_password(self, user: UserOut):
        # Return encrypted password from user object
        return user.hashed_password
        # return user["hashed_password"]

    def get_account_data_for_cookie(self, user: UserOut):
        # Return data for the cookie (two values)
        return user.email, UserOut(**user.dict())
        # return user["email"], UserOut(
        #     id=user["id"],
        #     email=user["email"],
        #     pickup_name=user["pickup_name"],
        #     phone_number=user["phone_number"],
        #     venmo=user["venmo"],
        #     role=user["role"],
        #     hashed_password=user["hashed_password"]
        # )


# set standard expiration time to two hours
two_hours = timedelta(hours=2)

authenticator = MyAuthenticator(
    os.environ["SIGNING_KEY"],
    exp=two_hours,
)

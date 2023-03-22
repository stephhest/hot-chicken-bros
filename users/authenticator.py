import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from datetime import timedelta
from queries.users import UserQueries
from models import UserOut, UserOutWithPassword


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        email: str,
        repo: UserQueries,
    ):
        # Use your repo to get the user based on email
        return repo.get(email)

    def get_account_getter(self, users: UserQueries = Depends()):
        # Return the users. That's it.
        return users

    def get_hashed_password(self, user: UserOutWithPassword):
        # Return encrypted password from user object
        return user.hashed_password

    def get_account_data_for_cookie(self, user: UserOut):
        # Return data for the cookie (two values)
        return user.email, UserOut(**user.dict())


# set standard expiration time to two hours
two_hours = timedelta(hours=2)

authenticator = MyAuthenticator(
    os.environ["SIGNING_KEY"],
    exp=two_hours,
)

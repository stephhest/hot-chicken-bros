from pydantic import BaseModel
from queries.pool import pool
from models import (
    UserIn,
    LoginForm,
    UserOut,
    UserOutWithPassword,
    Error,
    DuplicateUserError
)

class UserQueries(BaseModel):
    def get(self, email: str) -> UserOutWithPassword:
        pass

    def create(self, user: UserIn, hashed_password: str) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO users (
                            email,
                            hashed_password,
                            pickup_name,
                            phone_number,
                            venmo,
                            role
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            user.email,
                            hashed_password,
                            user.pickup_name,
                            user.phone_number,
                            user.venmo,
                            user.role
                        ],
                    )
                    id = cur.fetchone()[0]
                    return UserOutWithPassword(**cur.fetchone())
        except Exception as e:
            return Error(message=str(e))

    def update():
        pass

    def delete():
        pass

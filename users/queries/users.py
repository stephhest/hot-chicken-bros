from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool
from models import (
    UserIn,
    UserOut,
    Error
)

class UserQueries(BaseModel):
    # Get user by email (called in authenticator.py)
    def get(self, email: str) -> Union[UserOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id
                        , email
                        , pickup_name
                        , phone_number
                        , venmo
                        , role
                        , hashed_password
                        FROM users
                        WHERE email = %s;
                        """,
                        [email]
                    )
                    row = cur.fetchone()
                    if row:
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                        return record
                    else:
                        return Error(message="User not found")
        except Exception as e:
            print(e)
            return Error(message="Error getting user")

    def get_all(self) -> Union[List[UserOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id
                        , email
                        , pickup_name
                        , phone_number
                        , venmo
                        , role
                        , hashed_password
                        FROM users
                        ORDER BY id;
                        """
                    )
                    results = []
                    for row in cur.fetchall():
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                        results.append(record)
                    return results
        except Exception as e:
            print(e)
            return Error(message="Error getting users")

    def create(self, user: UserIn, hashed_password: str) -> UserOut:
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
                            venmo
                        ) VALUES (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            user.email,
                            hashed_password,
                            user.pickup_name,
                            user.phone_number,
                            user.venmo
                        ],
                    )
                    id = cur.fetchone()[0]
                    print("Created user with id: ", id)
                    user = UserOut(
                        id=id,
                        email=user.email,
                        pickup_name=user.pickup_name,
                        phone_number=user.phone_number,
                        venmo=user.venmo,
                        hashed_password=hashed_password
                    )
                    print("In create function, type of user: ", type(user))
                    return user
        except Exception as e:
            print(e)
            return {"message": "create did not work"}

    def update(self, user_id: int, input: UserIn, hashed_password: str) -> Union[bool, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE users
                        SET email = %s,
                            hashed_password = %s,
                            pickup_name = %s,
                            phone_number = %s,
                            venmo = %s,
                            last_modified = CURRENT_TIMESTAMP
                        WHERE id = %s
                        """,
                        [
                            input.email,
                            hashed_password,
                            input.pickup_name,
                            input.phone_number,
                            input.venmo,
                            user_id
                        ],
                    )
                    updated_row_count = cur.rowcount
                    if updated_row_count > 0:
                        print("Updated rows: ", updated_row_count)
                        return True
                    else:
                        print("Nothing to update.")
                        return False
        except Exception as e:
            print(e)
            return Error(message="Error updating user")

    def delete(self, user_id: int) -> Union[bool, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
                    deleted_row_count = cur.rowcount
                    if deleted_row_count > 0:
                        print("Deleted rows: ", deleted_row_count)
                        return True
                    else:
                        print("Nothing to delete.")
                        return False
        except Exception as e:
            print(e)
            return Error(message="Error deleting user")

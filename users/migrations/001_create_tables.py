steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(320) NOT NULL UNIQUE,
            phone_number VARCHAR(20) NOT NULL,
            venmo VARCHAR(50),
            role VARCHAR(50) NOT NULL DEFAULT 'User',
            hashed_password VARCHAR(200) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            password_last_modified TIMESTAMP
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ]
]

steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(320) NOT NULL UNIQUE,
            hashed_password VARCHAR(200) NOT NULL,
            pickup_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) NOT NULL,
            venmo VARCHAR(50),
            role VARCHAR(50) NOT NULL DEFAULT 'User',
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_modified TIMESTAMP
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ]
]

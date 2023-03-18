steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(320) NOT NULL UNIQUE,
            phone_number VARCHAR(20) NOT NULL,
            venmo VARCHAR(50) NOT NULL,
            role VARCHAR(50),
            password VARCHAR(200),
            hashed_password VARCHAR(200)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ]
]

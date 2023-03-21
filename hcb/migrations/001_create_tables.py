steps = [
    [
        # "Up" SQL statement - Menu Items Table
        """
        CREATE TABLE menu_items (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(250),
            price DECIMAL(5,2) NOT NULL DEFAULT 0.00,
            category VARCHAR(50),
            available BOOLEAN NOT NULL DEFAULT TRUE
        );
        """,
        # "Down" SQL statement - Menu Items Table
        """
        DROP TABLE menu_items;
        """,
    ],
    [
        # "Up" SQL statement - Heat Levels Table
        """
        CREATE TABLE heat_levels (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(250),
            score INT NOT NULL
        );
        """,
        # "Down" SQL statement - Heat Levels Table
        """
        DROP TABLE heat_levels;
        """,
    ],
    [
        # "Up" SQL statement - Events Table
        """
        CREATE TABLE events (
            id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR(100) NOT NULL,
            location VARCHAR(100) NOT NULL,
            date DATE NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL
        );
        """,
        # "Down" SQL statement - Events Table
        """
        DROP TABLE events;
        """,
    ],
    [
        # "Up" SQL statement - Pickup Slots Table
        """
        CREATE TABLE pickup_slots (
            id SERIAL PRIMARY KEY NOT NULL,
            event_id INT NOT NULL REFERENCES events(id) ON DELETE CASCADE,
            time TIME NOT NULL,
            max_mains INT NOT NULL,
            ordered_mains INT NOT NULL DEFAULT 0
        );
        """,
        # "Down" SQL statement - Pickup Slots Table
        """
        DROP TABLE pickup_slots;
        """,
    ],
    [
        # "Up" SQL statement - Carts Table
        """
        CREATE TABLE carts (
            id SERIAL PRIMARY KEY NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'In Progress',
            total DECIMAL(5,2) NOT NULL DEFAULT 0.00
        );
        """,
        # "Down" SQL statement - Carts Table
        """
        DROP TABLE carts;
        """,
    ],
    [
        # "Up" SQL statement - Cart Items Table
        """
        CREATE TABLE cart_items (
            id SERIAL PRIMARY KEY NOT NULL,
            cart_id INT NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
            menu_item_id INT NOT NULL REFERENCES menu_items(id),
            heat_level_id INT NOT NULL REFERENCES heat_levels(id),
            quantity INT NOT NULL DEFAULT 1
        );
        """,
        # "Down" SQL statement - Cart Items Table
        """
        DROP TABLE cart_items;
        """,
    ],
    [
        # "Up" SQL statement - Orders Table
        """
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY NOT NULL,
            existing_user_id INT,
            pickup_name VARCHAR(100) NOT NULL,
            customer_email VARCHAR(320) NOT NULL,
            customer_phone VARCHAR(20) NOT NULL,
            customer_venmo VARCHAR(50),
            cart_id INT NOT NULL REFERENCES carts(id),
            event_id INT REFERENCES events(id) ON DELETE CASCADE,
            pickup_slot_id INT REFERENCES pickup_slots(id),
            order_status VARCHAR(50) NOT NULL DEFAULT 'Placed',
            payment_status VARCHAR(50) NOT NULL DEFAULT 'Pending'
        );
        """,
        # "Down" SQL statement - Orders Table
        """
        DROP TABLE orders;
        """,
    ],
]

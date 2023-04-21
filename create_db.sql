
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    initials VARCHAR(255),
    date_of_birthday VARCHAR(255),
    age INTEGER,
    sex VARCHAR(30),
    email VARCHAR(255),
    phone VARCHAR(30) DEFAULT NULL,
    university VARCHAR(255) DEFAULT NULL,
    season VARCHAR(30) DEFAULT NULL,
    result INTEGER DEFAULT NULL
);

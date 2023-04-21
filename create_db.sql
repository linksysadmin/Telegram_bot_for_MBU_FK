
CREATE TABLE practice (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    date_of_birthday DATE,
    age INTEGER,
    sex TEXT,
    email TEXT,
    phone TEXT,
    university TEXT,
    season TEXT,
    test_result INTEGER
);

CREATE TABLE internship (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    date_of_birthday DATE,
    age INTEGER,
    sex TEXT,
    email TEXT,
    phone TEXT,
    university TEXT,
    season TEXT,
    test_result INTEGER
);

CREATE TABLE administrators (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id INTEGER PRIMARY KEY
);
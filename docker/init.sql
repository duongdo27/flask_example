CREATE DATABASE IF NOT EXISTS thea;

USE thea;

CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    token VARCHAR(255) NOT NULL,
    PRIMARY KEY (username)
);

INSERT INTO users (username, token)
VALUES ('duongdo@example.com', '12345');

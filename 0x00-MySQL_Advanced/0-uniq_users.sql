-- Creates a table users with the following fields:
-- id: integer, never null, auto increment and primary key
-- email: string (255 characters), never null and unique
-- name: string (255 characters)
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

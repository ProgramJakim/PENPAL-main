CREATE DATABASE IF NOT EXISTS social_media;

USE social_media;

-- Table for users
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    age INT,
    location VARCHAR(100),
    gender VARCHAR(10),
    interests TEXT,
    password VARCHAR(255)
);

-- Table for friendships (many-to-many relationship)
CREATE TABLE IF NOT EXISTS friendships (
    user1 VARCHAR(50),
    user2 VARCHAR(50),
    PRIMARY KEY (user1, user2),
    FOREIGN KEY (user1) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (user2) REFERENCES users(username) ON DELETE CASCADE
);

-- Table for friend requests
CREATE TABLE IF NOT EXISTS friend_requests (
    from_user VARCHAR(50),
    to_user VARCHAR(50),
    status ENUM('pending', 'accepted', 'rejected') DEFAULT 'pending',
    PRIMARY KEY (from_user, to_user),
    FOREIGN KEY (from_user) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (to_user) REFERENCES users(username) ON DELETE CASCADE
);

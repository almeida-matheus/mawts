-- Database: `aws.sqlite3`
CREATE DATABASE IF NOT EXISTS `aws`;
USE `aws`;

-- Table structure for table `user`
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    access_key TEXT NOT NULL UNIQUE,
    secret_key TEXT NOT NULL UNIQUE,
    passwd TEXT NOT NULL UNIQUE
);

-- Dumping data for table `user`
INSERT INTO user(access_key, secret_key, passwd)
VALUES('access_key', 'secret_key', 'passwd');
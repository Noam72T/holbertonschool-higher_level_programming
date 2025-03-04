-- Creates the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create Table states if it doesn't exist
-- Set id to auto increment and primary key
-- Set name to not null
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

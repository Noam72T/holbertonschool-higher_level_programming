-- Creates the user user_0d_1
-- If the user already exists, the script will not fail
-- Create user_0d_1 with all privileges
-- Set password to user_0d_1_pwd
-- Grant all privileges on all databases and tables

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

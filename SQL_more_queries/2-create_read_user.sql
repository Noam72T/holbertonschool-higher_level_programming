-- Create database if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant Only Select Privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush Privileges
FLUSH PRIVILEGES;

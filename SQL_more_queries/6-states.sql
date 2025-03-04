-- Create Table states
-- Set id to auto increment and primary key
-- Set name to not null

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

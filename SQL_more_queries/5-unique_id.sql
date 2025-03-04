-- Create Table unique_id
-- Set ID to default 1 and unique
-- Set name to not null

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

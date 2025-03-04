-- Creat Table id_not_null
-- Set ID to default 1
-- Set name to not null

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);


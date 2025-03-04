-- Create Table cities
-- Set id to auto increment and primary key
-- Set state_id to not null
-- Set name to not null
-- Set foreign key to states.id

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

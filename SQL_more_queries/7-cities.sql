-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Auto-generated unique ID
    state_id INT NOT NULL,                    -- Foreign key referencing states table
    name VARCHAR(256) NOT NULL,               -- City name, cannot be NULL
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

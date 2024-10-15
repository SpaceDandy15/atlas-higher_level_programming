-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Use the created database
USE hbtn_0e_0_usa;

-- Create the states table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert some records into the states table
INSERT INTO states (name) VALUES
('California'),
('Texas');

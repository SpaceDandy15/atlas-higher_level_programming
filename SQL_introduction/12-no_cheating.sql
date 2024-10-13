-- This script updates the score of Bob to 10 in the second_table
-- It uses only the name field to identify Bob

UPDATE second_table 
SET score = 10 
WHERE name = 'Bob';

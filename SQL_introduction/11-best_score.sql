-- This script lists all records from second_table with a score >= 10
-- Results are ordered by score in descending order

SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;

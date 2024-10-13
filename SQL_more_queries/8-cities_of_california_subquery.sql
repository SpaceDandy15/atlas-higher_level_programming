-- Select cities from California, ordered by city id
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    -- Subquery to get the id of the state where name is 'California'
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;

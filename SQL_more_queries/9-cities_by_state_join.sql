-- Lists all cities from the database hbtn_0d_usa
-- Displays city id, name, and state name
-- Results are sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

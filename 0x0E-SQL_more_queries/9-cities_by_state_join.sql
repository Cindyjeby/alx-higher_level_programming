-- Script that lists all cities contained int he database hbtn_0d_usa
-- Results must display cities.id - cities.name - state.name
-- Results must be sorted in ascending order by cities .id
-- Only one SELECT statement can be used

SELECT cities.id, cities.name,states.name
FROM cities
LEFT JOIN states  ON cities.state_id = states.id
ORDER BY cities.id ASC;

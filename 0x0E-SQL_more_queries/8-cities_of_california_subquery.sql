-- Script that lists all the cities of california that can be found in the database hbtn_0d_usa
-- The state table contains only one record where name = claifornia but the id can be different
-- Result must be sorted int ascending order by cities.id
-- Not allowed to use the join keyword

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'california'
)
ORDER BY id ASC;

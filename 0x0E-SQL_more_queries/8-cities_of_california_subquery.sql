-- Lists al the cities in California that can be found 
-- in the database hbtn_0d_usa

SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id=states.id AND states.name="Californi"
ORDER BY cities.id ASC;
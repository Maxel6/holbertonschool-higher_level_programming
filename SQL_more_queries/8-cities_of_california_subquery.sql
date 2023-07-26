-- lists all the cities of California that can be found in the database hbtn_0d_usa

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Get the state_id for California from the states table
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California from the cities table
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;
